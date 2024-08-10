# practicing taking input

# str_value = input('enter a string value:')
# print(str_value)
#
# # by default input returns string so type casting values
# int_value = int(input('enter a integer value:'))
# print(int_value)
#
# float_value = float(input('enter a float value:'))
# print(float_value)

# strings
str_value = 'Captain America'

# getting length of string
print(len(str_value))

#accessing string characters
print(str_value[2:4])

# accessing string values in reverse
print(str_value[::-1]) # here first value was start postion , second was end and last one was for step

# accessing the even characters of a string
print(str_value[::2])

# accessing odd characters of a string
print(str_value[1::2])

# splitting a string by spaces
print(str_value.split(' '))

# concatenating 2 strings
print('Hello'+'World')

# updating a value in a string --not possible string is immutable datatype
# str_value[3]='M'
# print(str_value)



# creating a list of 10 values
# lst = ['hello',1,2,3,'hi']
# print(lst)
#
# # updating a list value
# lst[1] = 'no'
# print(lst)
#
# # deleting single value from a list
# del lst[1]
# print(lst)
#
# # adding an element to the list in last position
# lst.append('cool')
# print(lst)
#
# # adding an element in begining of the list
# lst.insert(0,"i know ")
# print(lst)
#
# # adding an element in middle of the list
# lst.insert(len(lst)//2,"done")
# print(lst)
#
# # updating a list with elements from another list
# lst2 = [10,20,30]
# # append inserts the list as a single element
# # lst.append(lst2)
# # print(lst)
#
#
# # use extend for this purpose
# lst.extend(lst2)
# print(lst)
#
#
# # sorting a list in ascending order
# lst3 = [23,1,-1,234,431,100]
# lst3.sort()
# print(lst3)
#
# # sorting a list in descending order
# lst3.sort(reverse = True)
# print(lst3)

# merging two lists using zip