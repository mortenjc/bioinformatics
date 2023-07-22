import sys
sys.path.append('..')
import library as lib


e_coli = lib.readfile('../seqs/e_coli.txt')[0]
#print(lib.MinimumSkew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'))
print(lib.MinimumSkew(e_coli))
