class Person:
    id = None
    name =None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None


    def sleep(self):
        print('I am sleep method')

    def walk(self):
        print('I am walking')



class Dog:

    name = None
    breed = None
    color = None

    def __init__(self,name): # costructor cannot return anything
        # print('Automatically called')
        self.name= name
        # multiple constructor cant be created


    def sleep(self):
        print('sleeping')

    def bark(self):
        print('barking')


d1 = Dog('kamlesh')
d1.name = 'kamlesh'
print(d1.name)

d2 = d1
print(d2.name)

d2.name = 'Jaktu'
print(f'First :{d1.name} Now :{d2.name}')


'''
    Create a Employee Class
    A - name,age, phone, address, eid
    B - walk, talk, printdetails,
    with the Constructor which will set the values
    Ask the user about the information for E1, E2
    print the details of the E1, E2 via the print employee functions. 
'''
