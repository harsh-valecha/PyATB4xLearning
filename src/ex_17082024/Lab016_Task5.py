'''
### Task #5

- Create a program that takes two numbers as input and prints
 whether the first number is greater than, less than, or equal to the second number.
'''

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
if a>b:
    print('first number > second number')

elif a<b:
    print('first number < second number')

else:
    print('first number = second number')