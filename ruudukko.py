n = int(input())
column = []
for i in range (n):
    column.append(input().split())

routes = 0
def move(current):
    for nxtmove in row:
        if nxtmove < current:
            return move(nxtmove) + 1
    for nxtmove in column:
        if nxtmove[0] < current:
            return move(nxtmove[0]) + 1

for row in column:
    for start in row:
        routes = move(start)

ans = routes % (10**9+7)
print(ans)
