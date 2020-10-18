"""
GENERATORS
are a function that remembers the state it's in between executions
"""

def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i+=1

g = hundred_numbers()
print(next(g)) # go up to the yield -- the function remembers where it stopped

my_range_obj = range(10)
next(my_range_obj) # although it behaves like a g, it is not, and this would give back an error

print(list(g)) # this would list everything and print - notice it remembers how many g(s) you have already printed


"""
Generator Classes and iterators
are classes that have a __next__ method available
"""

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    
    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration() # tell python we reached the end of the generator


g = FirstHundredGenerator()
print(g.number)
# g.__next__() # this is what happens
next(g) # this makes it a generator
print(g.number)
print(next(g))


class FirstFiveIterator: # we don't generate numbers but return them from a list
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5] 
        self.i = 0

    
    def __next__(self):
        if self.i < len(self.numbers[self.i]):
            current = self.numbers[i]
            self.i += 1
            return current
        else:
            raise StopIteration()


"""
Iterables
are the ones we can loop through
"""