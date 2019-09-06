import os
os.chdir('C:/Users/yasha/Desktop/Python Programming/Rosalind/Data')

def hamming_distance(s,t):
    dist = 0
    for s_i, t_i in zip(s,t):
        if s_i == t_i:
            pass
        else:
            dist += 1
    return(dist)

with open("rosalind_hamm.txt", "r") as f:
    str1 = f.readline()
    str2 = f.readline()
    print(hamming_distance(str1, str2))
    
    
