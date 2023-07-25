import re
import Markup as mrk

# DNA codons -> Amino acids
codontab = {
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
    'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G'
}

# Return the amino acid for a DNA nucleotide sequence
def amino(nuclseq):
    assert len(nuclseq) == 3
    return codontab[nuclseq]

def aminoseq(nuclseq):
    s = ''
    for i in range(0, len(nuclseq), 3):
        s += amino(nuclseq[i:i+3])
    return s


def isStartCodon(aa):
    return aa == 'ATG'


def isStopCodon(aa):
    return aa == 'TAA' or aa == 'TAG' or aa == 'TGA'


def FindORF(dna, minlen):
    i = 0
    state = 0
    startindex = 0
    ORFs = []
    while True:
        codon = dna[i:i+3]
        if len(codon) != 3:
            break
        if state == 0: # looking for start
            if isStartCodon(codon):
                startindex = i
                state = 1
                i += 3
            else:
                i += 1
            continue
        elif state == 1: # protein
            if isStopCodon(codon):
                subseq = dna[startindex:i]
                if len(subseq) >= minlen:
                    ORFs.append([startindex, i+3])
                state = 0
            i += 3
            continue
    return ORFs
