import sys

#Store both input and output file names (CLI)
input_filename = sys.argv[1]
output_filename = sys.argv[2]

#Open and read sequences
input_file = open(input_filename)

#Create list of lines from file
sequences = input_file.readlines()

#Set up empty dict and integer to find longest line length
pos_dict = {}
longest_length = 0

#Set up loop to record line lengths and store position and base pairs
for line in sequences:

    line = line.strip()
    linelen = len(line)

    longest_length = linelen if (longest_length < linelen) else longest_length

    if ((linelen - 1) in pos_dict and pos_dict[linelen - 1] != line[0]):
        pos_dict[linelen - 1] = 'X'
        
    else:
        pos_dict[linelen - 1] = line[0]


#Should have populated dict by now, generate string
return_string = ''
for i in range(longest_length - 1, -1, -1):
    try:
        return_string += pos_dict[i]
    except KeyError:
        return_string += 'X'
    except:
        print("Something else went wrong")

#Write result to output file
output_file = open(output_filename, 'w')
output_file.write(return_string)

#Close all files to prevent memory leaks
input_file.close()
output_file.close()