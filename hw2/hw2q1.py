#Taken from website in hw resources
def phred33_to_q(qual):
  """ Turn Phred+33 ASCII-encoded quality into Phred-scaled integer """
  return ord(qual)-33

import sys

#Store both input and output file names (CLI)
input_filename = sys.argv[1]
output_filename = sys.argv[2]

#Open file to read
input_file = open(input_filename)


#Need to separate first three lines to get required info to set up count array
for i in range(3):
    input_file.readline() #Throw out first three lines

#Collect first quality sequence and record its length to create empty array to populate
first_line = input_file.readline().strip()
read_length = len(first_line) 
bad_quality_count = [0] * read_length

#Analyze first quality seq
for i in range(read_length):
   letter = first_line[i]
   score = phred33_to_q(letter)
   if (score < 10):
      bad_quality_count[i] += 1
      
#Continue with analying quality line every 3 lines
for line in input_file: #Prevents unnecessary memory usage by loading lines as needed
  for j in range(3):
    line = input_file.readline()

  line = line.strip()

  for i in range(read_length):
    letter = line[i]
    score = phred33_to_q(letter)
    if (score < 10):
        bad_quality_count[i] += 1

#Write array to output
output_file = open(output_filename, 'w')
for i in range(read_length):
   output_file.write(f"{bad_quality_count[i]}\n")

#Close all files to prevent memory leaks
input_file.close()
output_file.close()