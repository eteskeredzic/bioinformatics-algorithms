from itertools import product

def hamming(s1, s2):
    # assuming strings are same length
    rez = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            rez += 1
    return rez
    
def generateSimilar(s, d):
    li = ['A', 'T', 'C', 'G']
    l = [''.join(comb) for comb in product(li, repeat=len(s))]
    f = []
    for i in l:
        if hamming(i, s) <= d:
            f.append(i)
    return f

def nadji(pattern, dna, d):
    for i in range(len(dna) - len(pattern) + 1):
        s = dna[i:i+len(pattern)]
        if hamming(s, pattern) <= d:
            return True
    return False

def motifEnumeration(dna, k, d):
    patterns = set()
    for s in dna:
        for i in range(len(s) - k + 1):
            pattern = s[i:i+k]
            slicni = generateSimilar(pattern, d)
            for p in slicni:
                pojavljujeSe = True
                for s2 in dna:
                    pojavljujeSe = nadji(p, s2, d)
                    if pojavljujeSe == False:
                        break
                if pojavljujeSe == True:
                    patterns.add(p)
    return patterns
    
    
k = 3
d = 1
dna = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']

motifs = motifEnumeration(dna, k, d)
print(motifs)


