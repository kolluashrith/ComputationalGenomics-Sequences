
from io import TextIOWrapper

#Declare dictionary for use in function
LETTER_MATCH = {}


def find_pattern(outfile: TextIOWrapper, p: str, b: str, letters: list, ranks: list):
    """
    Helper function that runs backward search with BWT with the specified pattern.
    
     Args:
        outfile: output file object to write to, already opened
        p: pattern to compare
        b: BWT of text
        letters: array of offsets for each letter for use as column F
        ranks: ranks of each of the letters in the BWT b
    
    """

    outfile.write(f"{p} {b} ")

    comp_count = 1

    #Handle edge case if the last letter of P does not appear anywhere in the BWT
    if p[-1] not in LETTER_MATCH:
        outfile.write("-\n")
        return

    #Start traversing BWT
    curr_F_rows = list(range(letters[LETTER_MATCH[p[-1]]], letters[LETTER_MATCH[p[-1]] + 1]))

    #Loop to keep comparing through letters of pattern until either the search narrows to an empty array of indices or all letters are consumed
    while comp_count <= len(p):

        if len(curr_F_rows) == 0:
            outfile.write("-")
            break

        matches = [b[idx] for idx in curr_F_rows]
        rank_match = [ranks[k] for k in curr_F_rows]

        outfile.write(f"{''.join(matches)} ")

        comp_count += 1

        if comp_count > len(p):
            break #avoid filtering matches if we have nothing else to compare

        #Populate next set of indices to search
        curr_F_rows = []
        for w in range(len(matches)):
            if matches[w] == p[(-comp_count)]:
                int_map = LETTER_MATCH[matches[w]]
                curr_F_rows.append(letters[int_map] + rank_match[w])

    outfile.write("\n")
    return


import sys

#Store both input files and output file (CLI)
bwt_filename = sys.argv[1]
patterns_filename = sys.argv[2]
output_filename = sys.argv[3]

#Open files to read and write
bwt_file = open(bwt_filename)
patterns_file = open(patterns_filename)
output_file = open(output_filename, 'w')

#Store bwt
bwt = bwt_file.readline().strip()

alphabet = sorted(set(bwt))

LETTER_MATCH = {
    char: idx
    for idx, char in enumerate(alphabet)
}

#Store patterns
patterns = patterns_file.readlines()
patterns = [i.strip() for i in patterns] 

#Compute ranks and counts
Ldict = {}
rank = []
for letter in bwt:
    if letter not in Ldict:
        Ldict[letter] = 0

    #Store ranks 0-based and counts accurate simultaneously
    rank.append(Ldict[letter])
    Ldict[letter] += 1

Ldict = sorted(Ldict.items())
count = 0 
Larr = []

for m in Ldict:
    Larr.append(count)
    count += m[1]
Larr.append(count)       

for k in patterns:
    if not k:
        continue #in case an empty p slips through

    find_pattern(output_file, k, bwt, Larr, rank)

bwt_file.close()
patterns_file.close()
output_file.close()