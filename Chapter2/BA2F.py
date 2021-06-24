from random import randint

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


def randomizedMotifSearch(dna, k, t):
    motifs = []
    for i in dna:
        start = randint(0, len(i) - k)
        motifs.append(i[start:start + k])
    bestMotifs = motifs
    while True:
        profile = getProfile(motifs)
        motifs = []
        for i in dna:
            motifs.append(profileMostProbablekMer(i, k, profile))
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs
        else:
            return bestMotifs


k = 8
t = 5
dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
       'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
       'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
       'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
       'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

najbolji = float("Inf")
najboljiMotifs = []
for i in range(1000):
    x = randomizedMotifSearch(dna, k, t)
    trenutni = score(x)
    if trenutni <= najbolji:
        najbolji = trenutni
        najboljiMotifs = x

print(najboljiMotifs)



