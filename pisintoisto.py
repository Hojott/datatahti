dna = input()

length = []
l = 1


for i in range (len(dna)-1):
    if dna[i+1] == dna[i]:
        l = l + 1
        length.append(l)
    else:
        l = 1
        length.append(l)

if length != []:
    max = max(length)
else:
    max = 1

print(max)