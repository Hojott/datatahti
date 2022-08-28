input = input()

n = len(input)
wordlist = set()

for i in range (n):
    x = 1
    if x == n:
        word = input[i]
        wordlist.add(word)

    for j in range (n):
        x = 2
        if i!=j and x <= n:
            if x == n:
                word = input[i] + input[j]
                wordlist.add(word)

            for k in range (n):
                x = 3
                if k!=i and k!=j and x <= n:
                    if x == n:
                        word = input[i] + input[j] + input[k]
                        wordlist.add(word)

                    for l in range (n):
                        x = 4
                        if l!=i and l!=j and l!=k and x <= n:
                            if x == n:
                                word = input[i] + input[j] + input[k] + input[l]
                                wordlist.add(word)

                            for a in range (n):
                                x = 5
                                if a!=i and a!=j and a!=k and a!=l and x <= n:
                                    if x == n:
                                        word = input[i] + input[j] + input[k] + input[l] + input[a]
                                        wordlist.add(word)

                                    for b in range (n):
                                        x = 6
                                        if b!=i and b!=j and b!=k and b!=l and b!=a and x <= n:
                                            if x == n:
                                                word = input[i] + input[j] + input[k] + input[l] + input[a] + input[b]
                                                wordlist.add(word)

                                            for c in range (n):
                                                x = 7
                                                if c!=i and c!=j and c!=k and c!=l and c!=a and c!=b and x <= n:
                                                    if x == n:
                                                        word = input[i] + input[j] + input[k] + input[l] + input[a] + input[b] + input[c]
                                                        wordlist.add(word)

                                                    for d in range (n):
                                                        x = 8
                                                        if d!=i and d!=j and d!=k and d!=l and d!=a and d!=b and d!=c and x <= n:
                                                            if x == n:
                                                                word = input[i] + input[j] + input[k] + input[l] + input[a] + input[b] + input[c] + input[d]
                                                                wordlist.add(word)  

wordlistlist = list(wordlist)
wordlistlist.sort()
num = len(wordlistlist)

print(num)
for i in range(num):
    print(wordlistlist[i])
