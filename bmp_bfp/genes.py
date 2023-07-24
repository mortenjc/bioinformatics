
import library as lib
import Orf as orf


lines = lib.readfile('seqs/NC_000021.fasta')


dna = ''.join(lines[1:])
dna = dna.replace('\n', '')
print(len(dna))

res = orf.FindORF(dna, 250)
print(f'orfs: {res}')
