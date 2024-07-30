import copy

class Delicacy:
    def __init__(self , name , weight , price):
        self.name = name
        self.weight = weight
        self.price = price
        
    def __str__(self):
        return f"Delicacy(name: {self.name}, price: {self.price}, weight: {self.weight})"
    
candies = [
    Delicacy("Candy A", 2.50, 250),
    Delicacy("Candy B", 3.00, 400),
    Delicacy("Candy C", 1.75, 150),
    Delicacy("Candy D", 5.00, 500)
]

shallow_copy = copy.copy(candies)
deep_copy  = copy.deepcopy(candies)

for candy in shallow_copy:
    if candy.weight > 300:
        candy.price *= 0.8

for candy in deep_copy:
    if candy.weight > 300:
        candy.price *= 0.8


print('Original price:')
for candy in candies:
    print(candy)
    
print('Shallow Copy price:')
for candy in shallow_copy:
    print(candy)
    
print('Deep Copy price:')
for candy in deep_copy:
    print(candy)