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


x = generateSimilar('ACG', 1)

print(x)
