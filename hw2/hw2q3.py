import sys

#Store all arguments from command line
FASTA_filename = sys.argv[1]
FASTQ_filename = sys.argv[2]
output_filename = sys.argv[3]

#Open FASTA file to read and index
FASTA_file = open(FASTA_filename)

fastastart = FASTA_file.readline() #throw out first 
if (not fastastart.startswith(">")):
    FASTA_file.seek(0)

#Build 5-mer index
ref_kmer_dict = {}
k = 5

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
    offset_matches = []

    for i in range(4):
        read_segment = read[i*5:i*5+5]

        if (read_segment in ref_kmer_dict):
            offset_array = ref_kmer_dict[read_segment]

            for j in offset_array:
                mismatches = 0
                startpos = j - i*5

                #Verify that alignment is possible
                if startpos < 0 or startpos + len(read) > len(referenceseq):
                    continue

                good = True

                for l in range(len(read)):
                    if (read[l] != referenceseq[startpos + l]):
                        mismatches += 1
                        if (mismatches > 3):
                            good = False
                            break
                if (good and (startpos not in offset_matches)):
                    offset_matches.append(startpos)

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
