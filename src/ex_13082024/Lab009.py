name = 'harsh'
print(name.upper())
print(name.lower())
print(len(name))
print(name.swapcase())

a = '90'
print(type(a)) # string here!!
print(a.isnumeric())
kool = ['hi','hello','why']
print('-'.join(kool))

a = 23
# Return double of n
# def addition(n):
#     return n + n
#
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

def square(num):
    return int(num)**2

lst = input('enter values:').split(' ')
print(*list(map(square,lst)))
