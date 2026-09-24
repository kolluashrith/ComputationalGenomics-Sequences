import sys

def verify_position(startpos, read_length, ref_length):
    """Function to verify that the given starting position is a valid position by checking against reference sequence ranges"""
    if (startpos < 0 or startpos + read_length > ref_length):
        return False
    else:
        return True

def check_pos(pos, read, reference_seq):
    """Function to check if the given position could be the start to a valid alignment"""

    #Verify that alignment is possible
    mismatch_possible = verify_position(pos, len(read), len(reference_seq))

    mismatches = 0
    num_matched_bases_without_mismatch = 0

    #Check exact match or single mismatched pair
    if (mismatch_possible):
        for l in range(len(read)):
            if (read[l] != reference_seq[pos + l]):
                mismatches += 1
            elif mismatches == 0:
                num_matched_bases_without_mismatch += 1
            else:
                continue

            if mismatches > 1:
                break

        #Return yes if we have an exact match or one-off match
        if mismatches < 2:
            return True
    
    #Now, we check for deletions in the read
    
    deletion_possible = pos + len(read) + 1 <= len(reference_seq) #check that we can read one additional base

    if (deletion_possible):
        temp = num_matched_bases_without_mismatch
        for m in range(num_matched_bases_without_mismatch, len(read)):
            if (read[m] != reference_seq[pos + m + 1]):
                break
            else:
                num_matched_bases_without_mismatch += 1

            #Return yes if we have an single-deletion
        if num_matched_bases_without_mismatch >= len(read) - 1:
            return True
        else:
            num_matched_bases_without_mismatch = temp #reset

    #Now check insertion in read if needed. Make sure we can read there

    insertion_possible = verify_position(pos, len(read) - 1, len(reference_seq)) #less strict than single mismatch base

    if (insertion_possible):
        for g in range(num_matched_bases_without_mismatch + 1, len(read)):
            if (read[g] != reference_seq[pos + g - 1]):
                return False
        return True
    else:
        return False


def check_read(read, reference_dict, reference_seq):
    """Checks to see if the specified read can be found within one edit distance in the reference sequence, given the kmer dictionary"""

    for i in range(2):
        offset_array = []
        read_segment = read[i*10:i*10+10]

        #Get array of possible matches
        if (read_segment in reference_dict):
            offset_array = reference_dict[read_segment]

        for offset_candidate in offset_array:

            startpos = [offset_candidate - i*10 - 1, offset_candidate - i*10, offset_candidate - i*10 + 1]

            for pos in startpos:

                if check_pos(pos, read, reference_seq):
                    return True
                else:
                    continue
    return False

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
        if read == "":
            continue

        match = int(check_read(read, ref_kmer_dict, referenceseq))

        #Write 1 if found
        output_file.write(f"{match}\n")

        #Throw out lines 3 and 4
        FASTQ_file.readline()
        FASTQ_file.readline()


    output_file.close()
    FASTA_file.close()
    FASTQ_file.close()

    return

#Cody body that runs once command line calls script
FASTA_filename = sys.argv[1]
FASTQ_filename = sys.argv[2]
output_filename = sys.argv[3]
main(FASTA_filename, FASTQ_filename, output_filename)