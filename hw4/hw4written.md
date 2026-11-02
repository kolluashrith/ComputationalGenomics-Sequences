Ashrith Kollu

akollu1

1. ![hw4q1](/Users/ashrithkollu/Documents/Classes/Junior_Fall/ComputationalGenomics-Sequences/hw4/hw4q1written.png){ width=4.5in }\

2. ![hw4q2](/Users/ashrithkollu/Documents/Classes/Junior_Fall/ComputationalGenomics-Sequences/hw4/hw4q2written.png){ width=4.5in }\

3. ![hw4q3](/Users/ashrithkollu/Documents/Classes/Junior_Fall/ComputationalGenomics-Sequences/hw4/hw4q3written.png){ width=4.5in }\

4.
    a) With the linear gap penalty, alignment 1 costs 15 + 6 = 21. Alignment 2 costs 15.
    b) With the affine gap penalty, alignment 1 costs 7 + 6 = 13. Alignment 2 costs 15.
    c) We have alignment 1 cost o + 3 + 6 while alignment 2 cost is (o+1)*3. Solving some inequalities, we find that for o > 3, alignment 1 costs less than alignment 2. With o = 3, they cost the same, and o < 3 results in alignment 2 costing less. A biologist might prefer alignment 1 because consecutive gaps in alignments are more likely to occur than isolated ones like in alignment 2, so alignment 1 could be more scientifically relevant. 

5. 
    ![hw4q5p1](/Users/ashrithkollu/Documents/Classes/Junior_Fall/ComputationalGenomics-Sequences/hw4/hw4q5p1written.png){ width=4.5in }\
    ![hw4q5p2](/Users/ashrithkollu/Documents/Classes/Junior_Fall/ComputationalGenomics-Sequences/hw4/hw4q5p2written.png){ width=4.5in }\
    
6.
    a) ![hw4q6](/Users/ashrithkollu/Documents/Classes/Junior_Fall/ComputationalGenomics-Sequences/hw4/hw4q6written.png){ width=4.5in }\
    b) GTGGTGGAT -- length 9 as opposed to 10
    c) The first merge was the mistake. Taking the longest overlap first made the final superstring longer because of its effect on the second merge. Taking the longest one ensured an overlap of 4, but then the only other overlap was 1. This meant the final string length was only 5 letters shorter than the combined number of letters. On the other hand, if we took the shorter one, even though it would have had only 3 letters overlapping, it would have allowed for a second 3-letter overlap merge, bringing up the total difference to 6 letters shorter than the combined number of letters. Thus, this first greedy merge forced less optimal merges later on, making the superstring longer.