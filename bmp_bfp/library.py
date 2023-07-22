

def readfile(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


def PatternMatching(Pattern, Genome):
    positions = []
    pat_len = len(Pattern)
    for i in range(len(Genome) - pat_len + 1):
        if Genome[i:i+pat_len] == Pattern:
            positions.append(i)
    return positions

def PatternCount(Text, Pattern):
    count = 0
    plen = len(Pattern)
    for i in range(len(Text) - plen + 1):
        if Text[i:i + plen] == Pattern:
            count += 1
    return count


def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] += 1
    return freq


def FrequentWords(Text, k):
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    return [word for word in freq if freq[word] == m]


def SymbolArray(Genome, symbol):
    assert 0 == 1
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array


def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array


def Reverse(s1):
    return s1[::-1]


def Complement(seq):
    subs = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    res = ''
    for i in range(len(seq)):
        res += subs[seq[i]]
    return res


def ReverseComplement(seq):
    return Reverse(Complement(seq))


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
