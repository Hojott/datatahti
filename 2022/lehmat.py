map = input()
yx = map.split()
cows = 0
for i in range (int(yx[0])):
    toggle = 0
    reuna = 0
    row = input()
    byte = ""
    for j in range (int(yx[1])):
        oldbyte = byte
        byte = row[j]
        if byte == "*":
            if oldbyte == "*":
                reuna = 1
            else:
                if toggle == 0:
                    toggle = 1
                else:
                    toggle = 0
        elif byte == "@":
            if toggle == 1 and reuna == 0:
                cows +=1
 
print(cows)
