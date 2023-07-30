import sys
sys.path.append('../bmp_bfp')
import library as lib
import Replication as repl
import Markup as mrk
import matplotlib.pyplot as plt

dna = lib.readfile('../bmp_bfp/seqs/e_coli.txt')[0]
#dna = lib.readfasta('NC21b.fasta')

skewarr = repl.SkewArray(dna)
orics = repl.MinimumSkew(dna)

orici = orics[0]
oricdna = dna[orici-75:orici+600]
print(f'oriC at {orici} - showing {orici-75} - {orici+600}')
mrk.printSeq(oricdna)

fig, axs = plt.subplots(1,2)
axs[0].plot(list(skewarr.values()))
ymin, ymax = axs[0].get_ylim()
axs[0].vlines(x=[orici], ymin=ymin, ymax=ymax, color='red')

axs[1].plot(list(skewarr.values())[orici-75:orici+600])
ymin, ymax = axs[1].get_ylim()
axs[1].vlines(x=[75], ymin=ymin, ymax=ymax, color='red')
#axs[1].set_xlim([orici-75, orici+600])

plt.show()
