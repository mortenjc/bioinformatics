import sys, math
sys.path.append('..')

import Motif as mot


Profile = {
    'A' : [0.8, 0.0, 0.0, 0.2],
    'C' : [0.0, 0.6, 0.2, 0.0],
    'G' : [0.2, 0.2, 0.8, 0.0],
    'T' : [0.0, 0.2, 0.0, 0.8]
}
Dna = [
    'TTACCTTAAC',
    'GATGTCTGTC',
    'ACGGCGTTAG',
    'CCCTAACGAG',
    'CGTCAGAGGT'
]

res = mot.Motifs(Profile, Dna)
print(res)
