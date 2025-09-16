from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper


@my_decorator
def my_function():
    print("Inside function")


my_function()
print(my_function.__name__)  # should print "my_function"
