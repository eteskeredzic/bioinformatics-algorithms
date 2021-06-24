def PatternToNumber(s):
    mapa = {'A': 0,
            'C': 1,
            'G': 2,
            'T': 3}
    rez = 0
    for i in range(len(s)):
        rez = rez + mapa[s[i]] * 4 ** (len(s) - i - 1)
    return rez

def NumberToPattern(num, k):
    l = ['A', 'C', 'G', 'T']
    rez = ''
    for i in range(k-1, -1, -1):
        x = num // 4 ** i
        rez += l[x]
        num %= 4 ** i
    return rez
    
x = PatternToNumber('AGT')
x = NumberToPattern(x, 3)
print(x)
