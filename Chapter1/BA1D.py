def SubStringCount(Text, Pattern):
    l = []
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            l.append(i)

    return l
    
x = SubStringCount('GATATATGCATATACTT', 'ATAT')
print(x)
