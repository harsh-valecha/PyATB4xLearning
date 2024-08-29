# List - ordered collection of items
# can have heterogenous as well as homogenous elements
# length always start from 1
# index starts with 0

my_list=['kamlesh',1,2,4,5]
# print(my_list[0],my_list[2])

# list index out of range when no element present for
# spcified index

#printing elements
# print(my_list)
#
# # for loop can also be used
# for element in my_list:
#     print(element)

# reassigning
my_list[0]='Lankesh'

# adding new elements
my_list.append('rames')


# append cannot take mutiple elements at one time - append(1,2,3,4,...) does not work
my_list.extend([1,2,3,4,5])
print(my_list)

# inserting element at a specific position
my_list.insert(1,'Tullu') # on insertinng the elements will be shifted and not replaced
print(my_list)

my_list.insert(-1,'vilap')
print(my_list)

my_list.remove('rames')
print(my_list)

# creating a copy of list
lst2 = my_list.copy()
lst2[-1] = 'rada'
print(f'New list:{lst2}')
print(f'Old list:{my_list}')


lst3 = [10,-1,34,55]
# sorting
lst3.sort()
print(lst3)

lst4=['a','hula','baam']
lst4.sort()
print(lst4)

# for removing multiple elements use loop

# reversing order
print(f'Old list:{lst2}')
lst2.reverse()
print(f'After update:{lst2}')

# concatenation using +
print([1,2,3]+[4,5,6])