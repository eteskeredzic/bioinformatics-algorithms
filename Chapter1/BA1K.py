import itertools

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count = count + 1

    return count

def generateFrequencyArray(text, k):
    l = []
    for comb in itertools.product(['A', 'C', 'G', 'T'], repeat=k):
        l.append(''.join(comb))
        
    rez = []
    for i in l:
        print(i)
        rez.append(PatternCount(text, i))
    return rez
    
  
    
    
    
x = generateFrequencyArray("ACGCGGCTCTGAAA", 2)
print(x)
