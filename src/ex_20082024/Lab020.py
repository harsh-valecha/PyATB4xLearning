# max between 3 numbers
nums = list(map(int,input('Enter input in one line:').split(' ')))
print(nums)
num1 = nums[0]
num2 = nums[1]
num3 = nums[2]
if num1>num2 and num2>num3:
    print('num1 is greatest')
elif num2>num1 and num2>num3:
    print('num2 is greatest')
else:
    print('num3 is greatest')
