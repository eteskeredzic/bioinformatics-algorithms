
def suffix(s):
    return s[1:]

def prefix(s):
    return s[:-1]

def generateOverlapGraph(patterns):
    rez = []
    for i in range(len(patterns)):
        for j in range(len(patterns)):
            if i == j:
                continue
            if suffix(patterns[i]) == prefix(patterns[j]):
                rez.append((patterns[i], patterns[j]))
    rez.sort()
    return rez

patterns = ['ATGCG', 'GCATG', 'CATGC', 'AGGCA', 'GGCAT']

g = generateOverlapGraph(patterns)

for x in g:
    print(' -> '.join(x))
