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


def getProfile(motifs):
    kolone = len(motifs[0])
    profile = [[0] * kolone, [0] * kolone, [0] * kolone, [0] * kolone]
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


def greedyMotifSearch(dna, k, t):
    bestMotifs = []
    for s in dna:
        bestMotifs.append(s[0:k])

    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i + k]]

        for i in range(1, t):
            profile = getProfile(motifs)
            print(len(motifs))

            motifs.append(profileMostProbablekMer(dna[i], k, profile))
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs

    return bestMotifs


k = 3
t = 5
dna = ['GGCGTTCAGGCA',
       'AAGAATCAGTCA',
       'CAAGGAGTTCGC',
       'CACGTCAATCAC',
       'CAATAATATTCG']

x = greedyMotifSearch(dna, k, t)

print(x)

