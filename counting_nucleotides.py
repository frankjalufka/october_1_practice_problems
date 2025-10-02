
# save a nucleotide sequence as a variable
seq = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# create empty variables for each nucleotide count
a_count = 0
g_count = 0
c_count = 0
t_count = 0

# loop through the sequence, counting each A G C T
for nuc in seq:
    if nuc == "A":
        a_count += 1
    elif nuc == "G":
        g_count += 1
    elif nuc == "C":
        c_count += 1
    elif nuc == "T":
        t_count += 1

# print out the number of each nucleotide A G C T
print(a_count, c_count, g_count, t_count)

# advanced method using .count() string function
print(seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T"))

