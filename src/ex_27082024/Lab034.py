import time

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'time taken : {end_time-start_time}')
    return wrapper()

@time_decorator
def check_ui():
    print('Add a function to check how much time it takes')
    time.sleep(2)
