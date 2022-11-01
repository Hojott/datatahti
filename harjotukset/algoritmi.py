n = int(input())
ans = str(n) + " "

while n != 1:
    if (n % 2 == 0):
        n = int(n/2)
        ans = ans + str(n) + " "
    else:
        n = 3*n+1
        ans = ans + str(n) + " "

print(ans)