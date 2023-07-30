import random
import library as lib


def SlidingMatchCount(s1, s2, counts = {}):
    for i in range(len(s1)):
        subs1 = s1[-(i+1):]
        counts[i] = lib.CountMatches(subs1, s2)
    for i in range(len(s2)-1):
        subs2 = s2[i+1:]
        try:
            counts[i+len(s1)] += lib.CountMatches(s1, subs2)
        except:
            counts[i+len(s1)] = lib.CountMatches(s1, subs2)
    return(counts)


def ShuffledSlidingMatchCount(s1, s2, N=100):
    res = {}
    for i in range(N):
        s1_shuf = lib.Shuffle(s1)
        tmp = SlidingMatchCount(s1_shuf, s2, res)
        res = tmp
    for r in res:
        res[r] //= N
    return res
