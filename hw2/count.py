import sys

evo = sys.argv[1]
phix = sys.argv[2]

evo = open(evo)
phix = open(phix)

evocount = 0
phixcount = 0
totalreads = 0

for line in evo:
    if line.strip() == "1":
        evocount += 1
    totalreads += 1

for line in phix:
    if line.strip() == "1":
        phixcount += 1

print(f"Evo count = {evocount} \nPhix count = {phixcount} \nTotal reads = {totalreads}")