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
a class who ha the __iter__ method
"""

class SomeMoreIterables:
    def __iter__(self):
        return FirstHundredGenerator()

print(sum(SomeMoreIterables()))
print(list(SomeMoreIterables()))

for i in SomeMoreIterables():
    print(i)


# We can make the generator class an iterable like so:
class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    
    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


    def __iter__(self):
        return self


# we can loop through this
class AnotherIterable:
    def __init__(self):
        self.cars = ["Fiesta", "Focus"]


    def __len__(self):
        return len(self.cars)


    def __getitem__(self, i):
        return self.cars[i]
# the above is an iterable also
# in python we could use either the __iter__ dunder or both __len__ and __getitem__ to create an iterator (we can call next() on it)

for car in AnotherIterable():
    print(car)

# generator comprehension
my_numbers = [x for x in [1,2,3,4,5]] # it's a list
my_numbers_gen = (x for x in [1,2,3,4,5]) # it's a generator 

print(next(my_numbers_gen))


"""
filter() function
not very much used - best use comprehension
"""

def starts_with_f(friend):
    return friend.startswith("f")

friends = ["f1", "f2", "f3", "a1", "a2"]
with_f = filter(starts_with_f, friends) # arg1: function that returns True/False / arg2: iterable
#or
with_f = filter(lambda friend: friend.startswith("f"), friends) # and we could get rid of the function starts_with_f
# it could also be written as:
with_f = (friend for friend in friends if friend.startswith("f")) # generator comprehension which in most cases is faster than filter


print(next(with_f))


"""
map() function
takes an iterable and returns a new iterable
"""

friends_lower = map(lambda friend: friend.lower(), friends) # returns all names in the friends list in lowercase
friends_lower = [friend.lower() for friend in friends] # list comprehension would give us the same result but two different lists in memory
friends_lower = (friend.lower() for friend in friends) # generator comprehension would also give us the same result but be more efficient



"""
any() and all()
returns true if any/all element(s) of the list is True
"""

