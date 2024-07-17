# Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
# Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
# Apply your decorator to those functions to ensure that the time of the function executions can be monitored.


import datetime

def time_decorator(func):
    def wrapper(*args , **kwargs):
        
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(current_time)
        
        result = func(*args , **kwargs)
        return result
    return wrapper
    
@time_decorator
def add(a, b):
    return a + b

@time_decorator
def multiply(a, b):
    return a * b

@time_decorator
def greet(name):
    print(f"Hello, {name}!")
