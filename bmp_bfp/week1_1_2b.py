
def PatternCount(Text, Pattern):
    count = 0
    plen = len(Pattern)
    for i in range(len(Text) - plen + 1):
        if Text[i:i + plen] == Pattern:
            count += 1
    return count

v_cholerae_oric = [
'ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGAC',
'ATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGAT',
'TTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGG',
'CCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACT',
'TGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATA',
'ATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTC',
'TCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATG',
'ATCAAGCTGCTGCTCTTGATCATCGTTTC'
]

pat = 'TGATCA'

print(PatternCount(''.join(v_cholerae_oric), pat))