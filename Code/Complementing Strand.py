import os
os.chdir("C://Users//yasha//Desktop//Python Programming//Rosalind//Data")

def reverse_compl(seq):
    # find the reverse complement
    seq_split = list(seq.strip())
    rule = dict(zip('GACT', 'CTGA'))
    rev_compl = [rule[seq_split.pop()] for i in range(len(seq_split))]
    return(''.join(rev_compl))

    # alternative:
    # rev_compl = [rule[char] for char in reversed(seq)]

with open("rosalind_revc.txt", 'r') as file:
    print(reverse_compl(file.readline()))

