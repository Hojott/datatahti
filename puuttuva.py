n = int(input())
nums = input()

numlist = nums.split(' ')
numlist = list(map(int, numlist))
numlist.sort()

if n == 2:
    if numlist[0] == 1:
        print(2)
    if numlist[0] == 2:
        print(1)
else:
    if n != numlist[n-2]:
        print(n)
    else:
        for i in range (n-2):
            if numlist[i+1] != numlist[i]+1:
                print(numlist[i+1]-1)