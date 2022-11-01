from math import factorial, floor
from sys import set_int_max_str_digits

set_int_max_str_digits(3200000)

input = input()
digitsstr = input.split()
digits = [eval(i) for i in digitsstr]

i = digits[0]
while 1:
    i += 1
    lista = [0,0,0,0,0,0,0,0,0,0]
    fact = factorial(i)
    print(i)
    string = repr(fact)
    print(i)
    for j in string:
        lista[int(j)] +=1
        print(j)
    if lista == digits:
        print(i)
        exit()
    print(i)
