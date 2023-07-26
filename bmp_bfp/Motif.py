import random


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


def CountWithPseudocounts(Motifs):
    res = Count(Motifs)
    for key in res:
        for j in range(len(res[key])):
            res[key][j] += 1
    return res


def ProfileWithPseudocounts(Motifs):
    t = len(Motifs) + 4.0
    counts = CountWithPseudocounts(Motifs)
    for key in counts:
        arr = counts[key]
        counts[key] = [x/t for x in arr]
    return counts


def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    assert len(Dna) == t
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])

    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))

        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


def Motifs(Profile, Dna):
    res = []
    k = len(Profile['A'])
    for seq in Dna:
        res.append(ProfileMostProbableKmer(seq, k, Profile))
    return res


def RandomMotifs(Dna, k, t):
    assert len(Dna) == t
    l = len(Dna[0])
    res = []
    for seq in Dna:
        index = random.randint(0, l - k)
        res.append(seq[index:index+k])
    return res


def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M

    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs


def Normalize(Probabilities):
    norm  = 1.0/sum(Probabilities.values())
    for key in Probabilities:
        Probabilities[key] *= norm
    return Probabilities


def WeightedDie(Probabilities):
    keys = [k for k in Probabilities]
    values = [v for v in Probabilities.values()]
    return random.choices(keys, weights = values, k=1)[0]


def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)


def GibbsSampler(Dna, k, t, N):
    M = RandomMotifs(Dna, k, t)
    assert len(M) == t
    BestMotifs = M

    for j in range(N):
        i = random.randint(0, t-1)
        noti = [v for index, v in enumerate(M) if index != i]
        assert len(noti) == t - 1
        prof = ProfileWithPseudocounts(noti)
        kmer = ProfileMostProbableKmer(Dna[i], k, prof)
        noti.insert(i, kmer)
        M = noti
        assert len(M) == t
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
    return BestMotifs
