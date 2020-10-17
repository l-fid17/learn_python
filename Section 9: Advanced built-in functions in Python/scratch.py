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