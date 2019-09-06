import os
os.chdir("C://Users//yasha//Desktop//Python Programming//Rosalind//Data")

def rna_seq_maker(seq):
    # replace T with U
    return seq.replace("T", "U")


with open("rosalind_rna.txt", 'r') as f:
    print(rna_seq_maker(f.read()))