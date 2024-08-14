# create a Program I will give you number(userinput and print table)

num = int(input('Please enter the number :'))

print(f'{num} * 1 = {num*1}')
print(f'{num} * 2 = {num*2}')
print(f'{num} * 3 = {num*3}')
print(f'{num} * 4 = {num*3}')
print(f'{num} * 5 = {num*4}')
print(f'{num} * 6 = {num*5}')
print(f'{num} * 7 = {num*6}')
print(f'{num} * 8 = {num*7}')
print(f'{num} * 9 = {num*9}')
print(f'{num} * 10 = {num*10}')


#Create a program , take 2 inputs from the user num1, num2 and give them - max , pow , sub , mul
#sum , div ,formatting with fstring

num1 = int(input('Enter first number:'))
num2 = int(input('Enter secound number:'))

print(f'max of 2 num is :{max(num1,num2)}')
print(f'pow of num1 to num2 is :{pow(num1,num2)}')
print(f'subtracting num1 from num2:{num1-num2}')
print(f'multiplication of 2 numbers is :{num1*num2}')
print(f'sum of 2 numbers is :{num1+num2}')
print(f'division of 2 numbers is :{num1/num2}')
