import sys

def verify_position(startpos, read_length, ref_length):
    if (startpos < 0 or startpos + read_length > ref_length):
        return False
    else:
        return True

def check_read(read, reference_dict, reference_seq):
    offset_matches = []
    
    for i in range(2):
        offset_array = []
        read_segment = read[i*10:i*10+10]

        #Get array of possible starts
        if (read_segment in reference_dict):
            offset_array = reference_dict[read_segment]

        for offset_candidate in offset_array:

            mismatches = 0
            num_matched_bases = 0
            startpos = offset_candidate - i*10

            #Avoid rechecking found matches
            if startpos in offset_matches:
                continue

            #Verify that alignment is possible
            if not verify_position(startpos, len(read), len(reference_seq)):
                continue


            #First, check for full match or single mismatch
            mismatch_or_good = True

            for l in range(len(read)):
                if (read[l] != reference_seq[startpos + l]):
                    mismatches += 1
                elif mismatches == 0:
                    num_matched_bases += 1
                else:
                    continue

                if mismatches > 1:
                    mismatch_or_good = False
                    break

            #Now, we check for deletions in the read
            deletion = True

            if (startpos + len(read) + 1 <= len(reference_seq)):
                deletion = False

            if (not mismatch_or_good and deletion):
                for m in range(num_matched_bases, len(read)):
                    if (read[m] != reference_seq[startpos + m + 1]):
                        deletion = False
                        break
            

            #Now check insertion if needed. Make sure we can read there
            insertion = True
            if not verify_position(startpos, len(read) - 1, len(reference_seq)):
                insertion = False
            
            if (not mismatch_or_good and not deletion and insertion):
                for m in range(num_matched_bases+1, len(read)):
                    if (read[m] != reference_seq[startpos + m - 1]):
                        insertion = False
                        break

            if ((mismatch_or_good or insertion or deletion) and (startpos not in offset_matches)):
                offset_matches.append(startpos)

    return offset_matches



def main(FASTA_filename, FASTQ_filename, output_filename):
    #Store all arguments from command line
    

    #Open FASTA file to read and index
    FASTA_file = open(FASTA_filename)

    fastastart = FASTA_file.readline() #throw out first 
    if (not fastastart.startswith(">")):
        FASTA_file.seek(0)

    #Build 10-mer index
    ref_kmer_dict = {}
    k = 10

    offset = 0
    referenceseq = ""
    prev_k = ""

    for line in FASTA_file:
        line = line.strip()
        referenceseq = referenceseq + line

        sequence = prev_k + line

        #Build k-mers and add to dictionary
        for i in range(len(sequence) - k + 1):
            kmer = sequence[i:i+k]
            if kmer not in ref_kmer_dict:
                ref_kmer_dict[kmer] = [offset]
            else:
                ref_kmer_dict[kmer].append(offset)

            offset += 1

        #Overlap
        prev_k = sequence[-(k-1):]

    #Open FASTQ file to read and lookup partitions
    FASTQ_file = open(FASTQ_filename)

    output_file = open(output_filename, 'w')

    #Read FASTQ and perform alignment
    for _ in FASTQ_file:
        read = FASTQ_file.readline().strip() #throw out first, read second

        offset_matches = check_read(read, ref_kmer_dict, referenceseq)

        #Write every good offset in order
        offset_matches.sort()
        for num in offset_matches:
            output_file.write(f"{num} ")
        output_file.write("\n")

        #Throw out lines 3 and 4
        FASTQ_file.readline()
        FASTQ_file.readline()


    output_file.close()
    FASTA_file.close()
    FASTQ_file.close()

    return


FASTA_filename = sys.argv[1]
FASTQ_filename = sys.argv[2]
output_filename = sys.argv[3]
main(FASTA_filename, FASTQ_filename, output_filename)