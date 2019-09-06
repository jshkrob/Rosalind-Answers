import os
path = "C:/Users/yasha/Desktop/Python Programming/Rosalind/Data"
os.chdir('C:/Users/yasha/Desktop/Python Programming/Rosalind/Data')

def base_distribution(seq):
    bp = ['A','C','G','T']
    ls = [seq.count(char) for char in bp]
    char = bp[ls.index(max(ls))]

    return(ls, char)



def parse_fasta_(file):
    import numpy as np
    bp = ['A', 'C', 'G', 'T']

    # parsing DNA strings
    with open(os.path.join(path, file), "r", newline='') as f:
        # empty array for (A,T,C,G)
        data_matrix = []
        hasline = True

        line = f.readline().rstrip()
        while(hasline):
            if line.startswith('>'):
                id = line.strip('>')
                line = f.readline().rstrip()
                bp_sequence = ""

                while(line is not ''):
                    if not line.startswith('>'):
                        bp_sequence = bp_sequence + line
                        line = f.readline().rstrip()
                    else:
                        break
                data_matrix.append(list(bp_sequence)) # DNA string

            if(line == ''):
                print("Finished Parsing")
                hasline = False
        
        # creating profile
        len_seq = len(data_matrix[1])
        len_sample = len(data_matrix)
        profile, consensus = [], ""

        for i in range(len_seq):
            pos_i_string = []
            for j in range(len_sample):
                pos_i_string.append(data_matrix[j][i])
            distr_bp, consensus_bp = base_distribution(pos_i_string)

            # adding elements
            consensus += consensus_bp
            profile.append(distr_bp)
        
        # output as text file
        with open("output.txt", 'w') as output:
            # printing results:
            output.write("{}\n".format(consensus))
            for i in range(4):
                str_out = "{}: ".format(bp[i])

                # for each bp, print profile
                for j in range(len(profile)):
                    if j == len(profile) - 1:
                        str_out += ( str(profile[j][i]) + '\n' ) 
                    else:
                        temp = "{} ".format(str(profile[j][i]))
                        str_out += temp
                output.write(str_out)

if __name__ == '__main__':
    parse_fasta_("rosalind_cons.txt")

