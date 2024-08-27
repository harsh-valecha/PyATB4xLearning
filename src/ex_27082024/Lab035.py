# type conversions
# int , bool , float , complex , byte , str , list , dict

# lambda functions
o = lambda num:num**3
# print(o(10))


# limitation of lambda

def add(num):
    return num+10

print(add(100))

# converting to labda
o = lambda num:num+10
print(o(10))


# lambda with multiple arguments
o= lambda a,b:a*b
print(o(10,20))

o = lambda a,b,c:a+b+c
print(o(10,20,30))

# lambda with conditions
check_even_odd = lambda num:'Even' if num%2==0 else 'odd'
print(check_even_odd(23))

import math

op = lambda num:math.pow(int(input('Enter a number:')),2)
print(op(2))
