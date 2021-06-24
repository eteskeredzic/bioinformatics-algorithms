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

def getMinDistance(pattern, s):
    mini = float('inf')
    for i in range(len(s) - len(pattern) + 1):
        p = s[i:i+len(pattern)]
        if hamming(p, pattern) < mini:
            mini = hamming(p, pattern)
    return mini
    

def getSum(pattern, dna):
    suma = 0
    for i in dna:
        suma += getMinDistance(pattern, i)
    return suma   
    
  
# modificirano da vraca sve median stringove    
def medianString(dna, k, returnAll=False):
    mini = float('inf')
    najboljiPattern = ''
    if returnAll:
        najboljiPattern = []
        
        
    moguci = generateSimilar('AAA', k)
    for i in moguci:
        if returnAll == False:
            if getSum(i, dna) < mini:
                mini = getSum(i, dna)
                najboljiPattern = i
        else:
            if getSum(i, dna) <= mini:
                mini = getSum(i, dna)
                najboljiPattern.append(i)
    
    return najboljiPattern

    
k = 3
dna = ['AAATTGACGCAT',
       'GACGACCACGTT',
       'CGTCAGCGCCTG',
       'GCTGAGCACCGG',
       'AGTACGGGACAG']

st = medianString(dna, k, returnAll=True) 
print(st)    
