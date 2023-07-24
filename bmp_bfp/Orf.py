

def isStartCodon(aa):
    return aa == 'ATG'

def isStopCodon(aa):
    return aa == 'TAA' or aa == 'TAG' or aa == 'TGA'

def FindORF(dna, min):
    i = 0
    count = 0
    state = 0
    glen = 0
    start = 0
    while True:
        cod = dna[i:i+3]
        if len(cod) != 3:
            break
        assert len(cod) == 3
        if state == 0: # looking for start
            if isStartCodon(cod):
                start = i
                state = 1
                glen = 0
                i += 3
            else:
                i += 1
            continue
        elif state == 1: # protein
            if isStopCodon(cod):
                if glen > min:
                    print(f'start {start}, stop {i}')
                    count += 1
                state = 0

            else:
                glen += 1
            i += 3
            continue

    return count
