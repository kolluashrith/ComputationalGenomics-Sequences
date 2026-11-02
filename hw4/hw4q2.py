import sys, numpy as np

#Store both input and output file names (CLI)
input_filename = sys.argv[1]
output_filename = sys.argv[2]

#Open file to read and write
input_file = open(input_filename)
output_file = open(output_filename, 'w')

#Collect information in input file
x_seq = input_file.readline().strip()
y_seq = input_file.readline().strip()

def editDistance(x, y):

    V = np.zeros((len(x)+1, len(y)+1), dtype=int)

    Num_Optimal = np.ones((len(x)+1, len(y)+1), dtype=int)

    for i in range(len(x)+1):
        V[i, 0] = i
    for j in range(len(y)+1):
        V[0, j] = j
    
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            
            delt = 1 if x[i-1] != y[j-1] else 0
            V[i, j] = min(V[i-1, j-1] + delt, # diagonal
                            V[i-1, j  ] + 1,    # vertical
                            V[i  , j-1] + 1) # horizontal

            vertical_contribution = Num_Optimal[i-1][j] if (V[i-1, j  ] + 1 == V[i, j]) else 0
            horizontal_contribution = Num_Optimal[i][j-1] if (V[i, j-1] + 1 == V[i, j]) else 0
            diagonal_contribution = Num_Optimal[i-1][j-1] if (V[i-1, j-1] + delt == V[i, j]) else 0

            Num_Optimal[i][j] = vertical_contribution + horizontal_contribution + diagonal_contribution

    return V[len(x_seq), len(y_seq)], Num_Optimal[len(x_seq), len(y_seq)]


edits, alignments = editDistance(x_seq, y_seq)

output_file.write(f"{edits} {alignments}")

input_file.close()
output_file.close()