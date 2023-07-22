#
# Motif.py
#

def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    t = len(Motifs)

    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)

    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def Profile(Motifs):
    t = len(Motifs)
    counts = Count(Motifs)
    for key in counts:
        arr = counts[key]
        counts[key] = [x/t for x in arr]
    return counts


def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)

    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol

    return consensus


def Score(Motifs):
    cons = Consensus(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    assert k == len(cons)
    score = 0
    for i in range(k):
        for n in range(t):
            if cons[i] != Motifs[n][i]:
                score += 1
    return score


def Pr(Text, Profile):
    res = 1.0
    for i in range(len(Text)):
        res *= Profile[Text[i]][i]
    return res


def ProfileMostProbableKmer(text, k, profile):
    l = len(text)
    best = 0.0
    bestval = text[:k]
    for j in range(l - k + 1):
        kmer = text[j:j+k]
        s = Pr(kmer, profile)
        if s > best:
            bestval = kmer
            best = s
    return bestval


def GreedyMotifSearch(Dna, k, t):
    assert len(Dna) == t
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])

    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))

        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs
