import sys

#Store both input and output file names (CLI)
input_filename = sys.argv[1]
output_filename = sys.argv[2]

#Open file to read and write
input_file = open(input_filename)
output_file = open(output_filename, 'w')

#Collect information in input file
sequence = input_file.readline().strip()
seqlen = len(sequence)

#Create suffix array
suffixes = []
for i in range(seqlen):
    suffixes.append(sequence[i:])

suffixes = sorted(suffixes)
offsets = [(seqlen - len(suffixes[k])) for k in range(len(suffixes))]

towrite = ' '.join(str(item) for item in offsets) + '\n'
output_file.write(towrite)

#Find the BWT
bwt = [sequence[(element - 1) % seqlen] for element in offsets]
bwt_str = ''.join(bwt)
output_file.write(bwt_str)

#Count runs
idx = 0
count = 0
print(bwt_str)
print(f"\n{sequence}")
while idx < seqlen:
    curr = bwt_str[idx]
    
    count += 1

    while (idx + 1) < seqlen and bwt_str[idx + 1] == curr:
        idx += 1
    idx += 1
output_file.write(f"\n{count}")

output_file.close()
input_file.close()