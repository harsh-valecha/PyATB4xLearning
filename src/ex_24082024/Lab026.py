# program to return sum of three numbers

def sum_of_three_nums(num1,num2,num3):
    return num1+num2+num3

result = sum_of_three_nums(1,2,3)
# print(result)


# returning multiple values

def ret_mul(val1,val2):
    return val1,val2

# print(ret_mul(2,3)) # returns as tuple

def mul_args(*args):
    print(type(args))

mul_args()

