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
    l = [''.join(comb) for comb in product(li, repeat=len(li))]
    f = []
    for i in l:
        if hamming(i, s) <= d:
            f.append(i)
    return f

    
def mostFrequentWithMismatch(text, k, d):
    count = {}
    for i in range(len(text) - k + 1):
        slicni = generateSimilar(text[i:i+k], d)
        for kmer in slicni:
            if kmer in count:
                count[kmer] += 1
            else:
                count[kmer] = 1
    
    maks = max(count.values())
    return [kmer for kmer, c in count.items() if c == maks]    
    
x = mostFrequentWithMismatch("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)
print(x)
