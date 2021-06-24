
def suffix(s):
    return s[1:]

def prefix(s):
    return s[:-1]

def deBruijnFromKmers(patterns):
    pg = []
    for i in patterns:
        pg.append((prefix(i), suffix(i)))

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


patterns = [
    'GAGG',
    'CAGG',
    'GGGG',
    'GGGA',
    'CAGG',
    'AGGG',
    'GGAG']


g = deBruijnFromKmers(patterns)

for i in g:
    if type(i[1]) is tuple:
        print('{} -> {}'.format(i[0], ', '.join(i[1])))
    else:
        print('{} -> {}'.format(i[0], i[1]))
