import sys
sys.path.append('..')
import library as lib


e_coli=lib.readfile('../seqs/e_coli.txt')

#print(lib.SymbolArray('AAAAGGGG', 'A'))
print(lib.SymbolArray(e_coli[0], 'A'))
