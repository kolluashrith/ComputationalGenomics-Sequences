1. ![hw5q1](/Users/ashrithkollu/Documents/Classes/Junior_Fall/ComputationalGenomics-Sequences/hw5/hw5writtenq1.png){ width=4.5in }\
2. 
    a) At offset 40, there are at least 30 letters flanking both sides of the offset. Thus, 31 31-mers would have the error. At offset 95, only 4 letters flank the right side. Thus, 5 31-mers would have the error.
    
    b) Total nts = 3e9 * 30 = 9e10
       Errors = 9e10 * 0.01 = 9e8
       max_error_kmers = 9e8 * 31 = 2.79e10
       Distinct kmers in genome = 3e9 - 31 + 1 = 3e9 - 30
    
    c) 4^31 unique 31-mers exist in DNA, which is about 4.6e18. Thus, the fraction of possible kmers that are in the genome is only (3e9-30)/(4.6e18) which equals around 6.5e=10, an absurdly small number.
3. 
    a) The multigraph De Bruijn graph has one edge per 4-mer, so there are 152 edges in it. On the other hand, the edge-weighted graph only has one edge per *unique* 4-mer, so there are 31 edges in it.
    
    b) 
    c) For whole numbers less than 6 (i.e. 1, 2, 3, 4, 5), the tip and error bubble's extra path disappear since all the nodes associated with these extraneous structures have edge weights of 1 while those associated with heterozygous bubbles or the homozygous path have weights of 6 and 12, respectively. 
