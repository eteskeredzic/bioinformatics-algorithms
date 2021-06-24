def hamming(s1, s2):
    # assuming strings are same length
    rez = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            rez += 1
    return rez
    
x = hamming("GGGCCGTTGGT","GGACCGTTGAC")

print(x)
