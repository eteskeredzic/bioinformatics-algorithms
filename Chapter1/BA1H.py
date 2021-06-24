
def hamming(s1, s2):
    # assuming strings are same length
    rez = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            rez += 1
    return rez

def approxPatterns(pattern, text, d):
    l = []
    for i in range(len(text) - len(pattern) + 1): 
        if hamming(text[i:i + len(pattern)], pattern) <= d:
            l.append(i)
    return l
    
x = approxPatterns("ATTCTGGA", "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC", 3)

print(x)
