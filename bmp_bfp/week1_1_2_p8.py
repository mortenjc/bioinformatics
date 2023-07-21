

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

print(FrequentWords('CCCCCGATATATCCATAG',3))
