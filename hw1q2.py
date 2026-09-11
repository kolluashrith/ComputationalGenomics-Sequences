import sys

#Store both input and output file names (CLI)
input_filename = sys.argv[1]
output_filename = sys.argv[2]

#Open and read sequences, convert both to uppercase to avoid any issues with lowercase letters
input_file = open(input_filename)
sequence1 = input_file.readline().strip().upper()
sequence2 = input_file.readline().strip().upper()

#Probably redundant but just in case handling of inputs being read incorrectly
if len(sequence1) != len(sequence2):
    raise ValueError("Sequence lengths do not match")

#Count number of offsets
offsets_counter = 0
for i in range(len(sequence1)):
    if (sequence1[i] != sequence2[i]):
        offsets_counter += 1

#Write result to output file
output_file = open(output_filename, 'w')
output_file.write(str(offsets_counter))

#Close all files to prevent memory leaks
input_file.close()
output_file.close()
