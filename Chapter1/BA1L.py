def PatternToNumber(s):
    mapa = {'A': 0,
            'C': 1,
            'G': 2,
            'T': 3}
    rez = 0
    for i in range(len(s)):
        rez = rez + mapa[s[i]] * 4 ** (len(s) - i - 1)
    return rez

x = PatternToNumber('AGT')

print(x)
