
def minSkew(genome):
    l = [0]
    val = 0
    mini = 0
    for i in genome:
        if i == 'C':
            val = val - 1
        elif i == 'G':
            val = val + 1
        l.append(val)
        if val < mini:
            mini = val
    
    rez = []
    for i in range(len(l)):
        if l[i] == mini:
            rez.append(i)
    return rez
x = minSkew("CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG")
print(x)

