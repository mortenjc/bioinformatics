
def SkewArray(Genome):
    res = {}
    res[0] = 0
    for i in range(len(Genome)):
        if Genome[i] in 'AT':
            res[i+1] = res[i]
        elif Genome[i] == 'G':
            res[i+1] = res[i] + 1
        else:
            res[i+1] = res[i] - 1
    return res


def MinimumSkew(Genome):
    arr = SkewArray(Genome)
    minval = min(arr.values())
    res = []
    for i in range(len(arr)):
        if arr[i] == minval:
            res.append(i)
    return res


def HammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count


def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    pat_len = len(Pattern)
    for i in range(len(Text) - pat_len + 1):
        p = Text[i:i+pat_len]
        if HammingDistance(p, Pattern) <= d:
            positions.append(i)
    return positions


def ApproximatePatternCount(Pattern, Text, d):
    positions = ApproximatePatternMatching(Text, Pattern, d)
    return len(positions)
