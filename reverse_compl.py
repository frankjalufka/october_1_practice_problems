# input and save a dna sequence
dna = "AAAACCCGGT"

# create the reverse compliment strand of dna
rev_dna = dna.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g").upper()[::-1]

#print reversed compliment
print(rev_dna)
