from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, *kargs)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai():
    print("Brewing chai")

brew_chai()