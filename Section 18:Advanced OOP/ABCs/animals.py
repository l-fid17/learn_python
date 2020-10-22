"""
ABCs
"""
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta): # HERE!!!
    def walk(self):
        print("Walking...")

    # def num_of_legs(self):    # so we cut this and put it back into Dog
    #     return 4

    @abstractmethod
    def num_of_legs(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_of_legs(self): # although this could work for some animals it'll break if we want to extend an animal that does not have legs, a fish for example
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_of_legs(self): # this would overwrite the num_of_legs coming from the Animal class
        return 2

# however the below
a = Animal()
print(a.num_of_legs()) # will always return 4 (specified in the Animal class)
# but if we make it abstract it will return an error

# so we use ABCs -> see HERE!!!

# therefore now we can do
animals = [Dog("Rolf"), Monkey("Bob")]
for a in animals:
    print(isinstance(a, Animal))
    print(a.num_og_legs())