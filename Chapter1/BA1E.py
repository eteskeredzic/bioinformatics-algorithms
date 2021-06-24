def mostFrequent(text, k):
    count = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        if kmer in count:
            count[kmer] += 1
        else:
            count[kmer] = 1
    return count

def FindClumps(Genome, k, L, t):
    r = mostFrequent(Genome, k)
    l = []
    for i in r:
        print(i)
        if r[i] == t:
            l.append(i)
    return l
    
x = FindClumps('CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC', 5, 75, 4)
print(x)
