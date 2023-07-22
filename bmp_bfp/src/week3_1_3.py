import sys
sys.path.append('..')
import Motif as mot



motifs = ['AACGTA', 'CCCGTT', 'CACCTT', 'GGATTA', 'TTCCGG']

res = mot.Count(motifs)
print(res)

res = mot.Profile(motifs)
print(res)


res = mot.Consensus(motifs)
print(res)


res = mot.Score(motifs)
print(res)

text = 'ACGGGGATTACC'
prof = {
'A' : [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
'C' : [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
'G' : [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
'T' : [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
}

res = mot.Pr(text, prof)
print(res)


text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
k = 5
prof = {
'A' : [0.2, 0.2, 0.3, 0.2, 0.3],
'C' : [0.4, 0.3, 0.1, 0.5, 0.1],
'G' : [0.3, 0.3, 0.5, 0.2, 0.4],
'T' : [0.1, 0.2, 0.1, 0.1, 0.2]
}

res = mot.ProfileMostProbableKmer(text,k,prof)
print(res)

dna = [
'GGCGTTCAGGCA',
'AAGAATCAGTCA',
'CAAGGAGTTCGC',
'CACGTCAATCAC',
'CAATAATATTCG',
]
res = mot.GreedyMotifSearch(dna, 3,5)
print(res)
