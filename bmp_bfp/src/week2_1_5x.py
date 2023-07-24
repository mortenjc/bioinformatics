import sys
sys.path.append('..')
import library as lib
import Replication as repl
import Markup as mrk

e_coli = lib.readfile('../seqs/e_coli.txt')[0]
#print(lib.MinimumSkew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'))
res = repl.MinimumSkew(e_coli)
skew = res[0]
block = e_coli[skew:skew+500]
print(block)

words = lib.FrequentWords(block, 9)
offsets = []
for word in words:
    res = repl.ApproximatePatternMatching(block, word, 1)
    print(res)
    offsets += res
    res = repl.ApproximatePatternMatching(block, lib.ReverseComplement(word), 1)
    print(res)
    offsets += res

print(offsets)

lines = mrk.Format(block)
#print(lines)
mrk.Markup(lines, offsets, 9)
