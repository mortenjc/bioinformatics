#!/usr/local/bin/python3

import sys
sys.path.append('../bmp_bfp')
import library as lib
import Markup as mrk
import Protein as prt
import matplotlib.pyplot as plt
import numpy as np


def stats(data):
    n = len(data)
    avg = sum(data)/n
    maxval = max(data)
    ss = sum((x-avg)**2 for x in data)
    stddev = (ss/n)**0.5
    return maxval, avg, stddev


seqs = {'human'       : 'P69891', 'dog'       : 'P60524',
        'chicken'     : 'P01994', 'zebrafish' : 'Q90486',
        'jap_scallop' : 'A0A210PV81',
        'chimp'       : 'P68872'
       }


spec1 = 'chicken'
spec2 = 'jap_scallop'
path = '../bmp_bfp/seqs/hemoglobin'
dnaa = lib.readfasta(f'{path}/{seqs[spec1]}.fasta')
dnab = lib.readfasta(f'{path}/{seqs[spec2]}.fasta')
text = f'{spec1} - {spec2}'

#

fig, axs = plt.subplots(1,2)
fig.set_figwidth(14)
plt.suptitle(f'Hemoglobin comparison - {text}')

# I
res = prt.SlidingMatchCount(dnaa, dnab)
resarr = list(res.values())
maxval,a,s = stats(resarr)
print(maxval,a,s)
nbins = max(15, maxval//2)

n, bins, patches = axs[0].hist(resarr, nbins, histtype='bar')
patches[-1].set_facecolor('r')
ymin, ymax = axs[0].get_ylim()
axs[0].set_yscale('log')
axs[0].set_title('Sliding Match Count')


# II
res2 = prt.ShuffledSlidingMatchCount(dnaa, dnab, 300)
res2arr = list(res2.values())
maxval2,a2,s2 = stats(res2arr)
print(maxval2, a2, s2)
nbins = 7

axs[1].hist(res2arr, nbins, histtype='bar')
ymin, ymax = axs[1].get_ylim()
axs[1].set_yscale('log')
axs[1].set_title('Shuffled Sliding Match Count')
axs[1].vlines(x=[maxval], ymin=ymin, ymax=ymax, color='red')


plt.show()
