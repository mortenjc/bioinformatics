

def Format(seq):
    lines = []
    #print('         '.join(list(map(str,range(9)))))
    for i in range(0,len(seq),80):
        l = seq[i:i+80]
        lines.append(l)
    return lines


def isOffsetStart(i, offsets):
    for ofs in offsets:
        if ofs == i:
            return True
    return False


def isOffsetEnd(i, offsets, k):
    for ofs in offsets:
        if ofs + k == i:
            return True
    return False


def Markup(lines, offsets, k):
    print('<tt>')
    for l in range(len(lines)):
        pline = ''
        line = lines[l]
        for i in range(len(line)):
            if isOffsetStart(l*80 + i, offsets):
                pline += '<mark>'
            elif isOffsetEnd(l*80 + i, offsets, k):
                pline += '</mark>'
            pline += line[i]
        print(pline+'<br>')
    print('</tt>')
