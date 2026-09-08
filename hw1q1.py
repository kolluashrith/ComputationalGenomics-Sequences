import sys

#Store both input and output file names (CLI)
input_filename = sys.argv[1]
output_filename = sys.argv[2]

#Open and read sequence
input_file = open(input_filename)
sequence = input_file.readline()

#Define dictionary to store complementary pairs
complement = {
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C'
}

#Build reverse complement string one letter at a time
complement_string = ''
for i in range(len(sequence)-1, -1, -1):
    try:
        complement_string += complement[sequence[i]]
    except:
        continue #ignore any non-uppercase letters A, C, G, T

#Write result to output file
output_file = open(output_filename, 'w')
output_file.write(complement_string)

#Close all files to prevent memory leaks
input_file.close()
output_file.close()