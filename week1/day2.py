# practicing taking input

str_value = input('enter a string value:')
print(str_value)

# by default input returns string so type casting values
int_value = int(input('enter a integer value:'))
print(int_value)

float_value = float(input('enter a float value:'))
print(float_value)

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

# deleting a string
del str_value
# print(str_value)

# creating a raw string
raw_str = r'Hello world \n I am harsh'
print(raw_str)

# inserting string / numbers between a string
str_value = 'Hi this is %s'%'harsh'
print(str_value)

str_value = '%d + %d = %d'%(1,1,2)
print(str_value)

# here %d converts the float value to int value
str_value = '%f + %f = %d'%(1.1,1.1,2.2)
print(str_value)

# format method
print('Hi this is {name}'.format(name='harsh'))
print('Hi i have got some {} dollars can you give me {} rupees'.format(20,30))
print('There were only 2 people in class :{1},{0}'.format('Ram','Mahesh'))

name,age = 'elizabeta',2123
print('you know {} is {} years old'.format(name,age))
print('you know {person_name} is {person_age} years old'.format(person_name = name,person_age = age))

# fstrings
name = 'harsh'
batch = 'pyatb4x'
print(f'Hi this is {name} from {batch} batch')

# creating a list of 10 values
lst = ['hello',1,2,3,'hi']
print(lst)

# updating a list value
lst[1] = 'no'
print(lst)

# deleting single value from a list
del lst[1]
print(lst)

# adding an element to the list in last position
lst.append('cool')
print(lst)

# adding an element in begining of the list
lst.insert(0,"i know ")
print(lst)

# adding an element in middle of the list
lst.insert(len(lst)//2,"done")
print(lst)

# updating a list with elements from another list
lst2 = [10,20,30]
# append inserts the list as a single element
lst.append(lst2)
print(lst)


# use extend for this purpose
lst.extend(lst2)
print(lst)


# sorting a list in ascending order
lst3 = [23,1,-1,234,431,100]
lst3.sort()
print(lst3)

# sorting a list in descending order
lst3.sort(reverse = True)
print(lst3)

# merging two lists using zip