input = input()

i=1
j=1
while (i < len(input)):
    if (input[i] == ' '):
        a = input[0]
        while (j<i):
            a = a + input[j]
            j=j+1
        a = int(a)

        b = input[i+1]
        j = i+2
        while (j < len(input)):
            b = b + input[j]
            j=j+1
        b = int(b)

        break
    else:
        i=i+1

            

print(a+b)