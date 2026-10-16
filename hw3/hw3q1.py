comp_count = 0
present = False

def compare(seq, pat, comp_offset_idx, out_file):

  global comp_count

  for i in range(len(pat)):

    comp_count += 1

    comp_value = 0

    if seq[comp_offset_idx + i] > pat[i]:
      comp_value = -1
    if seq[comp_offset_idx + i] < pat[i]:
      comp_value = 1

    out_file.write(f"{comp_count} {i} {comp_offset_idx + i} {pat[i]} {seq[comp_offset_idx + i]}\n")

    if comp_value != 0:
      return comp_value
      
  return 0

import sys

#Store both input and output file names (CLI)
input_filename = sys.argv[1]
output_filename = sys.argv[2]

#Open file to read and write
input_file = open(input_filename)
output_file = open(output_filename, 'w')

#Collect information in input file
sequence = input_file.readline().strip()
offsets = input_file.readline().split()
pattern = input_file.readline().strip()

start_idx = 0
end_idx = len(offsets) - 1

while start_idx <= end_idx:
  
  mid_idx = (start_idx + end_idx) // 2

  c_val = compare(sequence, pattern, int(offsets[mid_idx]), output_file)

  if c_val > 0:
    start_idx = mid_idx + 1
  elif c_val < 0:
    end_idx = mid_idx - 1
  else:
    output_file.write("present")
    present = True
    break

if present == False:
  output_file.write("absent")


#Close all files to prevent memory leaks
input_file.close()
output_file.close()