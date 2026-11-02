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

def makeEditDistanceMatrices(x, y):

    MatchArray = np.zeros((len(x)+1, len(y)+1), dtype=int)
    XGapArray = np.zeros((len(x)+1, len(y)+1), dtype=int)
    YGapArray = np.zeros((len(x)+1, len(y)+1), dtype=int)

    for i in range(1, len(x)+1):
        MatchArray[i, 0] = 5 + i
        XGapArray[i, 0] = 5 + i
        YGapArray[i, 0] = 5 + i
    for j in range(1, len(y)+1):
        MatchArray[0, j] = 5 + j
        XGapArray[0, j] = 5 + j
        YGapArray[0, j] = 5 + j
    
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            delt = 3 if x[i-1] != y[j-1] else 0

            #Fill each array based on what the best next addition is and where the previous best came from
            MatchArray[i, j] = min(MatchArray[i-1, j-1] + delt, # Best alignment is match
                                XGapArray[i-1, j-1] + delt,  #Best alignment is x over gap
                                YGapArray[i-1, j-1] + delt) #Best alignment is y over gap
            XGapArray[i, j] = min(MatchArray[i-1, j] + 5,
                                XGapArray[i-1, j] + 1,
                                YGapArray[i-1, j] + 5)
            YGapArray[i, j] = min(MatchArray[i, j-1] + 5,
                                XGapArray[i, j-1] + 5,
                                YGapArray[i, j-1] + 1)

    return MatchArray, XGapArray, YGapArray

M, X, Y = makeEditDistanceMatrices(x_seq, y_seq)
#Bottom right element of each corresponds to match between last character of X and Y, a gap over X, and a gap over Y, respectively.

output_file.write(f"{M[len(x_seq), len(y_seq)]} {X[len(x_seq), len(y_seq)]} {Y[len(x_seq), len(y_seq)]}")

input_file.close()
output_file.close()
