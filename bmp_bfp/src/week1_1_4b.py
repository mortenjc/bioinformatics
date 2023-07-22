import sys
sys.path.append('..')
import library as lib


#print(PatternMatching('ATAT', 'GATATATGCATATACTT'))


v_cholerae = readfile('vibrio_cholerae.txt')[0]
print(PatternMatching('CTTGATCAT', v_cholerae))

t_petrofila = readfile('t_petrofila_ori.txt')[0]
print(PatternMatching('CTTGATCAT', t_petrofila))
print(PatternMatching('ATGATCAAG', t_petrofila))
