
def kmercomposition(k, text):
    rez = []
    for i in range(len(text)-k+1):
        rez.append(text[i:i+k])
    return rez


def getPathGraph(k, text):
    kmerManji = kmercomposition(k-1, text)
    rez = []
    for i in range(len(kmerManji)-1):
        rez.append((kmerManji[i], kmerManji[i+1]))
    rez.sort()

    return rez


def deBruijn(k, text):
    pg = getPathGraph(k, text)

    for i in range(len(pg)):
        for j in range(i+1, len(pg)-1):

            if pg[i][0] == pg[j][0]:
                pom = list((pg[i][1],))
                pom.append(pg[j][1])
                pom = tuple(sorted(pom))
                pg[i] = (pg[i][0], pom)
                del pg[j]
                j = j - 1
                i = i - 1
    pg.sort()
    return pg

k = 4
text = 'AAGATTCTCTAC'

g = deBruijn(k, text)

for i in g:
    if type(i[1]) is tuple:
        print('{} -> {}'.format(i[0], ', '.join(i[1])))
    else:
        print('{} -> {}'.format(i[0], i[1]))
