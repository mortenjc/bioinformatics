import sys
sys.path.append('..')
import library as lib



e_coli = lib.readfile('../seqs/e_coli.txt')[0]
#print(lib.MinimumSkew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'))
res = lib.MinimumSkew(e_coli)
skew = res[0]
block = e_coli[skew:skew+500]
print(block)

words = lib.FrequentWords(block, 9)
for word in words:
    res = lib.ApproximatePatternMatching(block, word, 1)
    print(res)
    res = lib.ApproximatePatternMatching(block, lib.ReverseComplement(word), 1)
    print(res)
