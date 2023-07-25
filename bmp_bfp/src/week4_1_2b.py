import sys, math, random
sys.path.append('..')

import Motif as mot

# I
Dna = [
    'TTACCTTAAC',
    'GATGTCTGTC',
    'ACGGCGTTAG',
    'CCCTAACGAG',
    'CGTCAGAGGT'
]

res = mot.RandomMotifs(Dna, 3, 5)
print(res)

# II
Dna = [
    'CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
    'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
    'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
    'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
    'AATCCACCAGCTCCACGTGCAATGTTGGCCTA'
    ]

res = mot.RandomizedMotifSearch(Dna, 8, 5)
print(res)
