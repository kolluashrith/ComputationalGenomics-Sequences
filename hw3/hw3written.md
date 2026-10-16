Ashrith Kollu
akollu1

1.  
    a) $CATCAT, T$CATCA, AT$CATC, CAT$CAT, TCAT$CA, ATCAT$C, CATCAT$ need to be sorted --> $CATCAT, AT$CATC, ATCAT$C, CAT$CAT, CATCAT$, T$CATCA, TCAT$CA. Taking the last column of each gives us TCCT$AA. Thus, BWT(T) = TCCT$AA

    b) <img src="https://raw.githubusercontent.com/kolluashrith/ComputationalGenomics-Sequences/refs/heads/main/hw3/hw3q1bwritten.png" alt="1b image" width="800">

    c) <img src="https://raw.githubusercontent.com/kolluashrith/ComputationalGenomics-Sequences/refs/heads/main/hw3/hw3q1cwritten.png" alt="1b image" width="800">
    With BWT GTA$T, we get an early termination of the reversal before all the letters are visited. Since the BWT of a string is a special permutation that allows for the reconstruction of the original string via reversal, the fact that the reversal failed on this string indicates that it is not a valid BWT. 

    



