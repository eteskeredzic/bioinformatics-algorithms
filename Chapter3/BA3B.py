
def genomePath(patterns):
    rez = patterns[0]
    for i in range(1, len(patterns)):
        rez += patterns[i][-1]
    return rez


patterns = ['ACCGA', 'CCGAA', 'CGAAG', 'GAAGC', 'AAGCT']

p = genomePath(patterns)
print(p)