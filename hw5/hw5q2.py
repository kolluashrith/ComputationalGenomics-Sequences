#ChatGPT was used to figure out how to get the sorting function at the end to use the indices as the key to sort. I still think lambdas are magic so it never occurs to me when they can be helpful...

import sys

#Store both input and output file names (CLI)
input_filename = sys.argv[1]
output_filename = sys.argv[2]

#Open file to read and write
input_file = open(input_filename)
output_file = open(output_filename, 'w')

#Collect information in input file
kmer = int(input_file.readline().strip())
lines = input_file.readlines()

#Need a data structure to store information about reads
class Node:
    """Class for creating a node that has the index, and its edges"""

    def __init__(self, index : int):
        self.idx = index
        self.edges = []
    
#Get dictionary that maps reads to nodes
read_node_dict = {}
for idx, line in enumerate(lines):
    sequence = line.strip()
    read_node_dict[sequence] = Node(idx)

#Calculate the magnitude of overlap between two given strings
def findoverlap(string1, string2):
    """Function that takes two strings and outputs the overlap between them"""
    seed = string2[0:kmer]
    indices = [i for i in range(len(string1)) if string1.startswith(seed, i)]

    if not indices:
        return -1

    for index in indices:
        curr = index
        if string2.startswith(string1[curr:]):
            return len(string1) - index
        else:
            continue
    #Here, there must have been no good suffix match
    return -1

#Find overlap between every single read pair greater than threshold specified
for string1 in read_node_dict.keys():
    for string2 in read_node_dict.keys():
        if string1 == string2:
            continue
        else:
            overlap = findoverlap(string1, string2)
            if overlap != -1:
                string1_node = read_node_dict[string1]
                string2_node = read_node_dict[string2]
                string1_node.edges.append((string2_node.idx, overlap))


# # FOR DEBUGGING, this thing prints all the edges
# for string in read_node_dict.keys():
#     idx = read_node_dict[string].idx
#     for element in read_node_dict[string].edges:
#         print(f"{idx} {element[0]} {element[1]}")


# Map node indices to Node objects
nodes_by_idx = {
    node.idx: node for node in read_node_dict.values()
}
# Store edges that are inferable
inf_edges = set()

# Check every possible two-edge path A -> B -> C
for node_a in nodes_by_idx.values():
    
    direct_paths = {
        dest for dest, overlap in node_a.edges
    } #Contains indices of all directly overlapped reads

    for b_idx, overlap_ab in node_a.edges:

        node_b = nodes_by_idx[b_idx]

        for c_idx, overlap_bc in node_b.edges:

            # If A -> C exists, it is inferable
            if c_idx in direct_paths:
                inf_edges.add((node_a.idx, c_idx))


# Remove inferable edges
for node in nodes_by_idx.values():

    node.edges = [
        (dest, overlap) for dest, overlap in node.edges if (node.idx, dest) not in inf_edges
    ]


# Write remaining edges in numerical order
for node in sorted(nodes_by_idx.values(), key=lambda n: n.idx):

    #python sorts by first element of tuple, so destination gets sorted too
    for dest, overlap in sorted(node.edges):
        output_file.write(f"{node.idx} {dest} {overlap}\n")


# Close files
input_file.close()
output_file.close()











