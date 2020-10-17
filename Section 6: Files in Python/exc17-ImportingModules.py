"""
# addition.py

class Addition:
    @classmethod
    def add(cls, num1, num2):
        return num1 + num2



"""
from addition import Addition


class Calculator:
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)

    @classmethod
    def subtract(cls, num1, num2):
        return Addition.add(num1, -num2)


    @classmethod
    def multiply(cls, num1, num2):
        tot = 0
        while num2 != 0:
            tot = Addition.add(tot, num1)
            num2 -= 1
        
        return tot

    @classmethod
    def divide(cls, num1, num2):
        tot = 0
        while num1 >= num2:
            tot = Addition.add(tot, 1)
            num1 = Addition.add(num1, -num2)
        
        return tot
            


print(Calculator.add(6, 2))             # 8
print(Calculator.subtract(6, 2))        # 4
print(Calculator.multiply(6, 2))        # 12
print(Calculator.divide(6, 2))          # 3