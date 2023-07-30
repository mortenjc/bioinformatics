import sys, math
sys.path.append('..')

import Motif as mot



prob = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}


norm = mot.Normalize(prob)
print(norm)


# II
prob2 = {'AA': 0.2, 'TT': 0.2, 'CC': 0.1, 'AT': 0.4}
res = mot.WeightedDie(prob2)

prof = {'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}
text = 'AAACCCAAACCC'
res = mot.ProfileGeneratedString(text, prof, 2)
print(res)
