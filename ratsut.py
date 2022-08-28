n = int(input())

if n == 0:
    ans = 0
else:
    ans = 0
    ans = ans + 4*(n**2 - (1+2))
    ans = ans + 8*(n**2 - (1+3))
    ans = ans + ((n-4)*4 + 4)*(n**2 - (1+4))
    ans = ans + ((n-4)*4)*(n**2 - (1+6))
    ans = ans + ((n-4)**2)*(n**2 - (1+8))

print(int(ans/2))