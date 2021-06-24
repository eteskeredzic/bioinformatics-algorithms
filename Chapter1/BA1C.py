def complement(text):
    rez = ''
    for i in text:
        if i == 'A':
            rez += 'T'
        elif i == 'T':
            rez += 'A'
        elif i == 'C':
            rez += 'G'
        else: 
            rez += 'C'
    return rez[::-1]
    
x = complement('AAAACCCGGT')

print(x)
