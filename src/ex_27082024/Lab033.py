# decorator

def my_decorator(func):

    def wrapper():
        print('something before')
        print('add helmet , gloves , kneeguard')
        func()
        print('something after')
        print('secure driving')
    return wrapper()

@my_decorator
def drive_bike():
    print('driving a bike')

# drive_bike() -- noneed as my decorator is already called
