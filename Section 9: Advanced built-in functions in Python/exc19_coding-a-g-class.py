"""
Coding Exercise 19: Exercise: coding a generator class
"""

# Define a PrimeGenerator class
# class PrimeGenerator:
#     # You may modify the __init__() method if necessary, but you don't need to change its arguments
#     def __init__(self, stop):
#         self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes


#     def __next__(self):
#         for n in range(2, self.stop):
#             for x in range(2, n):
#                 if n % x == 0:
#                     n += 1
#                     break
#                 else:
#                     return n
#             n+=1


# g = PrimeGenerator(100)

# while True:
#     print(next(g))

# class PrimeGenerator:
#     def __init__(self, stop):
#         self.stop = stop
#         self.n = 0    
    
#     def __next__(self):
#         if self.n < self.stop:
#             self.n += 1
#             for self.n in range(2, self.stop):
#                 for x in range(2, self.n):
#                     if self.n % x == 0:
#                         self.n += 1
#                 return self.n
#         else:
#             raise StopIteration()
 
# g = PrimeGenerator(50)
# while True:
#     print(next(g))

# class PrimeGenerator:
#     def __init__(self, stop):
#         self.stop = stop    
#         self.start = 2
    
#     def __next__(self):
#         for n in range(self.start, self.stop):
#             for x in range(2, n):
#                 if n % x == 0:
#                     break
#                 else:
#                     self.start = n + 1
#                     return n
#         raise StopIteration()            

# g = PrimeGenerator(100)
# while True:
#     print(next(g))

class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2
 
    def __next__(self):
        for n in range(self.start, self.stop):  # always search from current start (inclusive) to stop (exclusive)
            for x in range(2, n):
                if n % x == 0:      # not prime
                    break
            else:   # n is prime, because we've gone through the entire loop without having a non-prime situation
                self.start = n + 1  # next time we need to start from n + 1, otherwise we will be trapped on n
                return n    # return n for this round
        raise StopIteration()  # this is what tells Python we've reached the end of the generator


g = PrimeGenerator(100)
while True:
    print(next(g))