# read data from a file
def read_file(file_path): # reads a file and returns a list of lines in that file
    with open(file_path, "r") as f: 
        return [l.strip() for l in f.readlines()]

# create a function to calculate the GC content of a dna sequence
def gc_content(seq):
    return round(((seq.count("G") + seq.count("C")) / len(seq) * 100), 6)

FASTA_file = read_file("/Users/fljalufka/Downloads/rosalind_gc.txt") # read our data in from a file and store as a list of lines
FASTA_dict = {} # create an empty dictionary to store our key value pairs in
FASTA_label = "" # create an empty string to store the current label 

# convert our list of lines to a cictionary
for line in FASTA_file:
    if ">" in line:
        FASTA_label = line
        FASTA_dict[FASTA_label] = ""
    else:
        FASTA_dict[FASTA_label] += line

# format our data and pass into the gc_content function
# use dictionary comprehension to generate a new dictionary with the gc content
results_dict = {key: gc_content(value) for (key, value) in FASTA_dict.items()}

# identify the sequence with the highest gc content
max_GC_key = max(results_dict, key=results_dict.get)

# print out the label and gc content for the max gc key
print(f'{max_GC_key[1:]} \n{results_dict[max_GC_key]}')