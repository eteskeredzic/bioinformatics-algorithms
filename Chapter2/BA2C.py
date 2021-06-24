def profileMostProbablekMer(dna, k, profile):
    najboljep = -1
    rez = ''
    for i in range(len(dna) - k + 1):
        pattern = dna[i:i+k]
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
    
    
    
dna = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
k = 5
profile = [[0.2, 0.2, 0.3, 0.2, 0.3], # A 
           [0.4, 0.3, 0.1, 0.5, 0.1], # C
           [0.3, 0.3, 0.5, 0.2, 0.4], # G
           [0.1, 0.2, 0.1, 0.1, 0.2]] # T
           
s = profileMostProbablekMer(dna, k, profile)

print(s)
