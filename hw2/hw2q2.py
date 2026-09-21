import sys

#Store all arguments from command line
input_filename = sys.argv[1]
k = int(sys.argv[2])
output_filename = sys.argv[3]

#Open file to read
input_file = open(input_filename)

fastastart = input_file.readline() #throw out first 
if (not fastastart.startswith(">")):
    input_file.seek(0)

kmer_dict = {}
prev_k = "" #maintain k-1 previous characters to build kmer
offset = 0

for line in input_file:
    line = line.strip()

    sequence = prev_k + line

    #Build k-mers and add to dictionary
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer not in kmer_dict:
            kmer_dict[kmer] = [offset]
        else:
            kmer_dict[kmer].append(offset)

        offset += 1

    #Overlap
    prev_k = sequence[-(k-1):]

dup_counter = [0, 0] #first is distinct, second is unique

for element in kmer_dict:
    dup_counter[0] += 1

    if (len(kmer_dict[element]) == 1):
        dup_counter[1] += 1

output_file = open(output_filename, 'w')
output_file.write(f"{dup_counter[0]} {dup_counter[1]}")

input_file.close()
output_file.close()