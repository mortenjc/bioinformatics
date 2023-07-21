

def PatternCount(Text, Pattern):
    count = 0
    plen = len(Pattern)
    for i in range(len(Text) - plen + 1):
        if Text[i:i + plen] == Pattern:
            count += 1
    return count

assert PatternCount('GCGCG','GCG') == 2
