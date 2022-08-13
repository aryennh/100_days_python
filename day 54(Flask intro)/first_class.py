from time import sleep
def add(n1,n2) :
    return n1 + n2
def sub(n1,n2) :
    return n1-n2
def divide(n1,n2) :
    return n1//2
def multiply(n1,n2):
    return n1*n2
def calc(opr,n1,n2):
    return opr(n1,n2)

# print(calc(multiply,3,4))


def outer():
    print("im outer")

    def inner():
        print("im inner")

    return inner
# inner_function  = outer()
# inner_function()


#python decorator


def decorator_function(function):
    def wrapper():
        sleep(1)
        function()
        function()

    return wrapper

@decorator_function
def say_hello():
    print("Hello")

def say_bye():
    print("Bye")

say_hello()
say_bye()