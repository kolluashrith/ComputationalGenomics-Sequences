Ashrith Kollu

akollu1

1. ![hw5q1](/Users/ashrithkollu/Documents/Classes/Junior_Fall/ComputationalGenomics-Sequences/hw5/hw5writtenq1.png){ width=4.5in }\

2. 
    a) At offset 40, there are at least 30 letters flanking both sides of the offset. Thus, 31 31-mers would have the error. At offset 95, only 4 letters flank the right side. Thus, 5 31-mers would have the error.
    
    b) Total nts = 3e9 * 30 = 9e10  \
       Errors = 9e10 * 0.01 = 9e8   \
       max_error_kmers = 9e8 * 31 = 2.79e10 \
       Distinct kmers in genome = 3e9 - 31 + 1 = 3e9 - 30   \
    
    c) 4^31 unique 31-mers exist in DNA, which is about 4.6e18. Thus, the fraction of possible kmers that are in the genome is only (3e9-30)/(4.6e18) which equals around 6.5e-10, an absurdly small number.
3. 
    a) The multigraph De Bruijn graph has one edge per 4-mer, so there are 252 edges in it. On the other hand, the edge-weighted graph only has one edge per *unique* 4-mer, so there are 31 edges in it.
    
    b) There is a bubble that splits at node CAA which comes from the heterozygous site. This is evident from the edge weights down either pathway of the bubble. They both have nodes with edge weight 6, which is half of the weights of the nodes before the bubble. This suggests that half the reads came from one copy while the other half came from the other copy. These rejoin at node GTG. There is also a bubble that splits at the node GTT. This likely comes from a sequencing error since the edge weights down one path is 11 while the edge weights down the other is 1. This split is significantly different than half, and the lone k-mers suggest that it came from a source other than the actual genome. Thus, this is most likely from an error. These rejoin at node CTG. The two kmers at the heterozygous site are CAAC and CAAA. 


    c) For whole numbers less than 6 but greater than 1 (i.e. 2, 3, 4, 5), the tip and error bubble's extra path disappear since all the nodes associated with these extraneous structures have edge weights of 1 while those associated with heterozygous bubbles or the homozygous path have weights of 6 and 12, respectively. 
