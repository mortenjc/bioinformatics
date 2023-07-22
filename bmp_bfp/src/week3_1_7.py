import sys, math
sys.path.append('..')
import Motif as mot


profile = {

    'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
    'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
    'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
    'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
}

def EntropyScore(profile):
    entropy = 0.0
    l = len(profile['A'])
    for i in range(l):
        for c in 'ACGT':
            val = profile[c][i]
            if  val != 0.0:
                entropy += val * math.log2(val)
    return -entropy


print(EntropyScore(profile))
