input = input()
input = input.split(' ')
y = int(input[0])
x = int(input[1])

if y%2 == 0:
    if x <= y:
        ans = y**2 - (x-1)
    else:
        if x%2 == 1:
            ans = x**2 - (y-1)
        if x%2 == 0:
            ans = (x-1)**2 + y #(x-1)**2 + 1 + (y-1)
if y%2 == 1:
    if x <= y:
        ans = (y-1)**2 + x #(y-1)**2 + 1 + (x-1)
    else: #same as above
        if x%2 == 1:
            ans = x**2 - (y-1)
        if x%2 == 0:
            ans = (x-1)**2 + y #(x-1)**2 + 1 + (y-1)

print(ans)