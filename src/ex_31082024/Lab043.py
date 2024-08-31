'''
    Create a Employee Class
    A - name,age, phone, address, eid
    B - walk, talk, printdetails,
    with the Constructor which will set the values
    Ask the user about the information for E1, E2
    print the details of the E1, E2 via the print employee functions.
'''

class Employee:
    __eid = 1
    def __init__(self,name,age,phone,address):
        self.name = name
        self.eid = Employee.__eid
        Employee.__eid+=1
        self.age = age
        self.phone = phone
        self.address = address

    def walk(self):
        print(f'{self.name} is walking')

    def talk(self):
        print(f'{self.name} is talking')

    def printdetails(self):
        print(f'id is {self.eid} , name is {self.name} , age is {self.age} , phone is {self.phone} , address is {self.address}')

    def __repr__(self):
        return self.name

employees = []
for i in range(2):
    name = input('Please provide name:')
    age = int(input('Please provide age:'))
    phone = int(input('Provide phone :'))
    address = input('Provide address : ')
    employees.append(Employee(name,age,phone,address))
    employees[i].walk()
    employees[i].talk()
    employees[i].printdetails()

print(employees)
'''
Please provide name:Kamlesh
Please provide age:23
Provide phone :5676868
Provide address : Bhojpur
Kamlesh is walking
Kamlesh is talking
id is 1 , name is Kamlesh , age is 23 , phone is 5676868 , address is Bhojpur
Please provide name:Jaktap
Please provide age:45
Provide phone :7987897897
Provide address : Jalgaon
Jaktap is walking
Jaktap is talking
id is 2 , name is Jaktap , age is 45 , phone is 7987897897 , address is Jalgaon
[Kamlesh, Jaktap]
'''
