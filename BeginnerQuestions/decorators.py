#decorator function takes a function as its parameter
def uppercase_decorator(func):
    #The wrapper function 
    def wrapper():
        uppercase = func().upper()
        return uppercase
    return wrapper

#decorated function
@uppercase_decorator
def lambdatest():
    return "Mobile apps and cross browser testing cloud"

print(lambdatest())

python -m venv <venv_name>