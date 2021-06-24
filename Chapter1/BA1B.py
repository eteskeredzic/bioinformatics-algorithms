from BA1A import PatternCount

def mostFrequent(text, k):
    count = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        if kmer in count:
            count[kmer] += 1
        else:
            count[kmer] = 1
    
    maks = max(count.values())
    return [kmer for kmer, c in count.items() if c == maks]
    
x = mostFrequent('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4)

print(x)
