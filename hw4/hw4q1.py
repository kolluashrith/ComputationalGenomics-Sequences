import sys, numpy as np 

def overlapAlignment(x, y):

    #Construct DP matrix with the specified penalties and bonuses

    V = np.zeros((len(x)+1, len(y)+1), dtype=int)

    #Can start at any suffix of x, so comparing any element of x to empty string yields 0. First column should be all 0.

    for j in range(len(y)+1):
        #Since alignment must start at Y[0], any gaps in alignment at the start of y needs to be penalized
        V[0, j] = -2*j

    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            delt = 1 if x[i-1] == y[j-1] else -2
            V[i, j] = max(V[i-1, j-1] + delt, # diagonal
                          V[i-1, j  ] - 2,    # vertical
                          V[i  , j-1] - 2) # horizontal
    return V


#Store both input and output file names (CLI)
input_filename = sys.argv[1]
output_filename = sys.argv[2]

#Open file to read and write
input_file = open(input_filename)
output_file = open(output_filename, 'w')

#Collect information in input file
x_seq = input_file.readline().strip()
y_seq = input_file.readline().strip()

#Extract the last row of X, which corresponds to full alignments of X (any suffix)
V = overlapAlignment(x_seq, y_seq)
interesting_scores = V[len(x_seq)]

max_score = max(interesting_scores) #get the best score
col = np.where(interesting_scores == max_score)[0][-1] #Get the last col with the best score; this is the longest prefix of Y with the best score

output_file.write((f"{col} {max_score}"))

input_file.close()
output_file.close()