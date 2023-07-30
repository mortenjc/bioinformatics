#!/usr/local/bin/python3

import sys
sys.path.append('../bmp_bfp')
import library as lib
import Markup as mrk
import Protein as prt
import matplotlib.pyplot as plt
import numpy as np


haemo_dog='VHLTAEEKSLVSGLWGKVNVDEVGGEALGRLLIVYPWTQRFFDSFGDLSTPDAVMSNAKVKAHGKKVLNSFSDGLKNLDNLKGTFAKLSELHCDKLHVDPENFKLLGNVLVCVLAHHFGKEFTPQVQAAYQKVVAGVANALAHKYH'
haemo_hum='MGHFTEEDKATITSLWGKVNVEDAGGETLGRLLVVYPWTQRFFDSFGNLSSASAIMGNPKVKAHGKKVLTSLGDAIKHLDDLKGTFAQLSELHCDKLHVDPENFKLLGNVLVTVLAIHFGKEFTPEVQASWQKMVTAVASALSSRYH'
haemo_dog_shuffled = lib.Shuffle(haemo_dog)


#
# res = prt.SlidingMatchCount(haemo_dog, haemo_hum)
# print(max(res.values()))
# print(res[10], res[11], res[12], res[12])
#
# res = prt.SlidingMatchCount(haemo_dog_shuffled, haemo_hum)
# print(max(res.values()))
# print(res[10], res[11], res[12], res[12])


res = prt.ShuffledSlidingMatchCount("ABCDEFG", "AXCDDEF", 10)
print(max(res.values()))
print(res)
