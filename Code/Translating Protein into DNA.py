import os
os.chdir('C:/Users/yasha/Desktop/Python Programming/Rosalind/Data')

table = { 
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T', 
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                  
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P', 
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R', 
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A', 
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G', 
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S', 
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L', 
        'UAC':'Y', 'UAU':'Y', 'UAA':'Stop', 'UAG':'Stop', 
        'UGC':'C', 'UGU':'C', 'UGA':'Stop', 'UGG':'W', 
        } 

def rna_to_protein(seq):
    amino_seq = ""
    stop_codon = False
    if (len(seq) % 3 == 0):
        for i in range(0, len(seq), 3):
            codon = table[seq[i:i+3]]
            if codon is not 'Stop':
                amino_seq = amino_seq + codon
    return(amino_seq)

# with open("rosalind_prot.txt", 'r') as f:
#     print(rna_to_protein(f.readline().rstrip()))
#    # print(rna_to_protein(f.readline()))


def finding_motif(s, t):
    for i in range(len(s) - (len(t) - 1)):
        if t == s[i:i+len(t)]:
            print(i+1, end = " ")

finding_motif("ACGCGATTCATACGCGATAGACGCGATCTTACGCGATGCAATGCTACGCGATTGATCCACGCGATACGCGATGATACGCGATATTACGCGATGGTGTCACGCGATTTTGCAACTACGCGATCAGTACGCGATACGCGATACCTACGCGATACGCGATACACGCGATACGCGATACGCGATCGACGCGATACGCGATCGTTACGCGATACGCGATCAAATTTGTTGTTGCGCACGCGATACGCGATACACGCGATCCAATACGCGATAGTACGCGATATACGCGATACGCGATTACACGCGATACGCGATAACGCGATGACGCGATTTAGGACGCGATCTCAACGCGATACGCGATGACGCGATACGCGATGATAGGGAACGCGATTGACGCGATACGCGATAACACGCGATGCTGATCTACGCGATTCGTACGCGATAGACGCGATTCAACGCGATCCTATACAGCAAGACTCGACGCGATCGAAACGCGATACGCGATACGCGATACACGCGATGTGTGACGCGATGCGGGTGGGCCACTAACGCGATCAACGCGATATCGTGTTGGCGTAAGTGGAGAAAACGCGATACGCGATACGCGATCGTTATACGCGATCACGCGATAACGCGATAAGATACGCGATAGTACGCGATACGCGATACCAAAACGCGATTTACGCGATATAATCGAAACGACGCGATACTATACGCGATTACGCGATAACGCGATGGTTACGCGATGATACGCGATTACGCGATAACGCGATCCCTAACGCGATTCACCACGCGATAGACGCGATGACGCGATTACGCGATTCCCTCACGGCCACGCGATCGGGACGCGATACGCGATTACGCGATACGCGATGACGCGATCGGAACGCGATTGTGGACGCGATTACCTGTGACGCGATACACGCGATGGAAGTACGCGATGCACGCGATACACGCGATGACGCGATACGCGATAAGGACGCGAT",
"ACGCGATAC")
