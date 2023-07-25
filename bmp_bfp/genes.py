
import library as lib
import Orf as orf
import Markup as mrk


def printORFs(dna, orfs, long=False, protseq=False):
    print(f'candidates found: {len(orfs)}')
    prev = 0
    for elt in orfs:
        if protseq:
            prt = orf.aminoseq(dna[elt[0]:elt[1]])
            short = prt[:30] + '  ...  ' + prt[-30:]
        else:
            short = ''
        gap = elt[0] - prev
        print(f'gap {gap:6} - start {elt[0]}, end {elt[1]}, len (nt|aa) ({elt[1]-elt[0]:4}|{(elt[1]-elt[0])//3:4}) - {short}')
        prev = elt[1]
        if long:
            mrk.printSeq(dna[elt[0]:elt[1]])

#
# #
#


#lines = lib.readfile('seqs/NC_000021.fasta')
lines = lib.readfile('seqs/SYNJ1.fasta')
dna = ''.join(lines[1:])
#lines = lib.readfile('seqs/dosr.txt')
#dna = ''.join(lines)
dna = dna.replace('\n', '')
#rdna = lib.ReverseComplement(t)

print('FindORF')

#orfs = orf.FindORF(dna, 9)
orfs = orf.FindORF(dna, 50)

printORFs(dna, orfs, long=True, protseq=False)

#print(dnaclean[-50000:])
