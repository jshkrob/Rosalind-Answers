
import os
print(os.getcwd())
os.chdir('C:/Users/yasha/Desktop/Python Programming/Rosalind/Data')
print(os.getcwd())

def count_nt(data):
	dict = {}
	for nt in data:
		if nt not in dict:
			dict[nt] = 1
		else:
			dict[nt] += 1
	print('{} {} {} {}'.format(dict['A'], dict['C'], dict['G'], dict['T']))

dict = {'a':1, 'b':2, 'c':3}
print('a' not in dict)

count_nt('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')

with open('rosalind_dna.txt', 'r') as f:
	for line in f:
		count_nt(line)



