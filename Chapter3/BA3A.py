
def kmercomposition(k, text):
    rez = []
    for i in range(len(text)-k+1):
        rez.append(text[i:i+k])
    rez.sort()
    return rez


k = 5
text = 'CAATCCAAC'

x = kmercomposition(k, text)

print(x)


