import random

def readfile(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


def readfasta(filename):
    lines = readfile(filename)
    dna = ''.join(lines[1:])
    dna = dna.replace('\n', '')
    return dna


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
    subs = {'A':'T', 'T':'A', 'C':'G', 'G':'C',
            'B':'V', 'V':'B', 'D':'H', 'H':'D',
            'K':'M', 'M':'K', 'S':'S', 'W':'W', 'N':'N', 'R':'R'}
    res = ''
    for i in range(len(seq)):
        res += subs[seq[i]]
    return res


def ReverseComplement(seq):
    return Reverse(Complement(seq))


def CountMatches(s1, s2):
    #print(s1, s2)
    res = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            res += 1
    return res


# Knuth shuffle
def Shuffle(s1):
    n = len(s1)
    ls1 = list(s1)
    for i in range(n):
        r = random.randint(i, n - 1)
        ls1[i], ls1[r] = ls1[r], ls1[i]
    return ''.join(ls1)
