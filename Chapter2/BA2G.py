from random import randint
from random import random

def profileMostProbablekMer(dna, k, profile):
    najboljep = -1
    rez = ''
    for i in range(len(dna) - k + 1):
        pattern = dna[i:i + k]
        kolona = 0
        trenutnop = 1
        for c in pattern:
            red = 0
            if c == 'C':
                red = 1
            elif c == 'G':
                red = 2
            elif c == 'T':
                red = 3
            trenutnop *= profile[red][kolona]
            kolona = kolona + 1

        if trenutnop > najboljep:
            najboljep = trenutnop
            rez = pattern

    return rez


def getProfile(motifs, pseudocount=1):
    kolone = len(motifs[0])
    profile = [[pseudocount] * kolone, [pseudocount] * kolone, [pseudocount] * kolone, [pseudocount] * kolone]
    for i in range(len(motifs[0])):
        for j in range(len(motifs)):
            if motifs[j][i] == 'A':
                profile[0][i] += 1
            elif motifs[j][i] == 'C':
                profile[1][i] += 1
            elif motifs[j][i] == 'G':
                profile[2][i] += 1
            else:
                profile[3][i] += 1
    return profile


def score(motifs):
    profile = getProfile(motifs)
    score = 0
    ukupno = len(motifs)

    for i in range(len(profile[0])):
        maksi = 0
        for j in range(len(profile)):
            if profile[j][i] > maksi:
                maksi = profile[j][i]

        score += ukupno - maksi

    return score

def Random(p):
    suma = sum(p)
    for i in range(len(p)):
        p[i] /= suma
    suma = 0
    rez = 0
    izbor = random()
    for x in p:
        suma += x
        if izbor < suma:
            return rez
        rez += 1


def profileRandomlyGeneratedKmer(dna, profile):
    l = []
    ukupno = profile[0][0] + profile[1][0] + profile[2][0] + profile[3][0]
    for i in range(len(dna) - len(profile[0]) + 1):
        pattern = dna[i:i+len(profile[0])]
        p = 1.
        for j in range(len(pattern)):
            k = 3
            if pattern[j] == 'A':
                k = 0
            elif pattern[j] == 'C':
                k = 1
            elif pattern[j] == 'G':
                k = 2

            p *= float(profile[k][j]) / ukupno
        l.append(p)
    pocetniIndeks = Random(l)
    return dna[pocetniIndeks:pocetniIndeks+len(profile[0])]


def gibbsSampler(dna, k, t, N):
    motifs = []
    for i in dna:
        start = randint(0, len(i) - k)
        motifs.append(i[start:start + k])
    bestMotifs = motifs
    for j in range(0, N):
        ii = randint(0, t-1)
        profile = getProfile([motif for x, motif in enumerate(motifs) if x != ii])
        motifs[ii] = profileRandomlyGeneratedKmer(dna[ii], profile)
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs
        else:
            return bestMotifs


k = 8
t = 5
N = 100
dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
       'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
       'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
       'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
       'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

najbolji = []
najbolji_score = float('Inf')
for i in range(20):
    x = gibbsSampler(dna, k, t, N)
    if score(x) <= najbolji_score:
        najbolji_score = score(x)
        najbolji = x

print(najbolji)
print(najbolji_score)

# posto je random, ne nalazi nuzno najbolji moguci rezultat