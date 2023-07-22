import sys
sys.path.append('..')
import library as lib


assert lib.Reverse('ABCDE') =='EDCBA'
assert lib.Complement('ATGC') =='TACG'
assert lib.ReverseComplement('ATCG') == 'CGAT'
