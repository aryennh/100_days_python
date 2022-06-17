import kwargs as kwargs


def add(*args):
    sum = 0
    for n in args:
        sum+=n
    return sum

import tkinter

#KWARGS - > keyword arguments
#keyword arguments can be accessed by name
#kwargs is basically a dictionary
"""def calculate(n, **kwargs):
    #print(kwargs)
    #print(type(kwargs))
    #for key,value in kwargs.items():
        #print(key)
        #print(value)
        print(kwargs['add'])

    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(2, add=3,multiply=5)"""
"""
print(add(1,4,6,3,1))
print(add(4,2))
"""

class Car :
    def __init__(self,**kwargs):
        self.make = kwargs['make']
        self.model = kwargs['model']

my_car = Car(make="Nissan")
print(my_car.model)
