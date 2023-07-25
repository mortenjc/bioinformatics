import sys, math
sys.path.append('..')
import Motif2 as mot2




motifs = [
    'AACGTA',
    'CCCGTT',
    'CACCTT',
    'GGATTA',
    'TTCCGG'
]

res = mot2.CountWithPseudocounts(motifs)
print(res)
print('Part II')

dna = [
    'GGCGTTCAGGCA',
    'AAGAATCAGTCA',
    'CAAGGAGTTCGC',
    'CACGTCAATCAC',
    'CAATAATATTCG'
]
res = mot2.GreedyMotifSearchWithPseudocounts(dna, 3, 5)
print(res)
