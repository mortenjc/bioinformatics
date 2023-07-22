import sys
sys.path.append('..')
import library as lib


e_coli=lib.readfile('../seqs/e_coli.txt')

#print(lib.SymbolArray('AAAAGGGG', 'A'))
res = lib.FasterSymbolArray(e_coli[0], 'A')
print(f'len: {len(res)}, first {987}:{res[987]}, {988}:{res[988]}')
print(res)
