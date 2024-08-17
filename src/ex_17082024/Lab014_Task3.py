### Task #3


#- Explain the difference between the = operator and the == operator in Python.
'''
 = operator is used for assignment of literal to a variable while == operator is used
for equality between two values / variables / expressions

'''

# using = operator
var1 = 100

# using == operator -- returns boolean value True /False after comparison
print(True==False)
# example 2
print(2+3 == 5)


#- What does the ** operator do in Python, and how is it used?

'''
** operator is used as an alternative of pow
'''
print(2**3)
# can also be used to assign power to a variable or expression
x = 23
print(x**2)

# example 3
a= 1
b = 2
print((a+b)**2)

print(f'Proving the formula for (a+b)**2 : '
      f'{(a+b)**2== (a)**2+ (b)**2 + 2*a*b}')

#- What does the ^ operator do in Python, and in what context is it commonly used?

'''
^ is also known as XOR operator
Truth table - 
A	B	A⊕B
1	1	0
0	1	1
1	0	1
0	0	0
'''

a = True
b = False

print(a^b)

# practicing on numbers
a = 17
print(f'binary value of a is :{bin(a)[2:]}')

b = 23
print(f'binary value of b is :{bin(b)[2:]}')

# expected should be 00110
print(f'XOR of a and b is :{bin(a^b)[2:]}')
print(f'converting to decimal value : {int(bin(a^b)[2:],2)}')




