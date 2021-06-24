
def hamming(s1, s2):
    # assuming strings are same length
    rez = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            rez += 1
    return rez


def distanceBetweenPatternAndStrings(pattern, dna):
    k = len(pattern)
    distance = 0
    for s in dna:
        ham = float('Inf')
        for i in range(len(s) - k + 1):
            patternp = s[i:i+k]
            if ham > hamming(pattern, patternp):
                ham = hamming(pattern, patternp)
        distance = distance + ham
    return distance





pattern = "AAA"

dna = ['TTACCTTAAC',
       'GATATCTGTC',
       'ACGGCGTTCG',
       'CCCTAAAGAG',
       'CGTCAGAGGT']

x = distanceBetweenPatternAndStrings(pattern, dna)

print(x)