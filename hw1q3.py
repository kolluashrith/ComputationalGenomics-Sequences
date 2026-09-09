import sys

#Store both input and output file names (CLI)
input_filename = sys.argv[1]
output_filename = sys.argv[2]

#Open and read sequences
input_file = open(input_filename)
sequence = input_file.readline().strip()

#Map each amino acid to its number of possible codons
num_codons = {
    'F': 2,
    'L': 6,
    'I': 3,
    'M': 1,
    'V': 4,
    'S': 4,
    'P': 4,
    'T': 4,
    'A': 4,
    'Y': 2,
    'H': 2,
    'Q': 2,
    'N': 2,
    'K': 2,
    'D': 2,
    'E': 2,
    'C': 2,
    'W': 1,
    'R': 6,
    'S': 2,
    'G': 4
}

#Initialize count at 3 to account for stop codons and start multiplying
count = 3
for i in sequence:
    try:
        count *= num_codons[i]
    except:
        if (i == '*'): 
            break #Sequence ends at stop codon
        else:
            continue #Redundant handling of extraneous inputs

#Write result to output file
output_file = open(output_filename, 'w')
output_file.write(str(count))

#Close all files to prevent memory leaks
input_file.close()
output_file.close()