#ChatGPT was used at the very end to catch any final bugs and its only contribution was pointing out I left in some debugging print statements by accident.

import sys
from collections import defaultdict

#Store both input and output file names (CLI)
input_filename = sys.argv[1]
output_filename = sys.argv[2]

#Open file to read and write
input_file = open(input_filename)
output_file = open(output_filename, 'w')

#Collect information in input file
kmer = int(input_file.readline().strip())
lines = input_file.readlines()

#Need a data structure to store in degrees and out degrees to find where to start
class Node:
    """Class for creating a node that has data, the next and previous links, and the degrees"""

    def __init__(self, data : str):
        self.data = data
        self.prev = set()
        self.next = set()

def getNode(data, dict):
    """Function that gets a node associated with a string if it exists or makes one if it doesn't"""

    if data not in dict:
        dict[data] = Node(data)

    return dict[data]


#Graph construction
kmer_node_dict = {}

for line in lines:
    line = line.strip()
    for i in range(len(line) - kmer + 1):

        from_node = getNode(line[i:i+kmer-1], kmer_node_dict)
        to_node = getNode(line[i+1:i+kmer], kmer_node_dict)

        from_node.next.add(to_node)

        to_node.prev.add(from_node)

#Assemble graphs into contigs
def assemble(start, next_node, contig_list):

    curr_node = next_node
    start += curr_node.data[-1]

    while len(curr_node.next) == 1 and len(curr_node.prev) == 1:
        curr_node = next(iter(curr_node.next), None)
        start += curr_node.data[-1]
    contig_list.append(start)
    return
    

contig_list = []
for node in kmer_node_dict.values():

    #Do not start with any simple nodes
    if len(node.next) == 1 and len(node.prev) == 1:
        continue

    string = node.data
    curr_node = node

    for next_node in curr_node.next:
        assemble(string, next_node, contig_list)

contig_list.sort()

for contig in contig_list:
    output_file.write(f"{contig}\n")

#Close files
input_file.close()
output_file.close()
