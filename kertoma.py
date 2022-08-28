import math

n = int(input())
zero = 0

while n >= 5:
    n = n/5
    zero = zero + math.floor(n)
    
print(zero)