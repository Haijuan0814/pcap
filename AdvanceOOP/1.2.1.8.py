# Scenario
# Imagine that you receive a task description of an application that monitors the process of apple packaging before the apples are sent to a shop.

# A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

# Write a code that creates objects representing apples as long as both limitations are met. When any limitation is exceeded, than the packaging process is stopped, and your application should print the number of apple class objects created, and the total weight.

# Your application should keep track of two parameters:

# the number of apples processed, stored as a class variable;
# the total weight of the apples processed; stored as a class variable. Assume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;
# Hint: Use a random.uniform(lower, upper) function to create a random number between the lower and upper float values.


import random
class Apple:
    total_apples = 0
    total_weight = 0.0
    
    def __init__(self):
        
        self.weight = random.uniform(0.2, 0.5)
        Apple.total_apples += 1
        Apple.total_weight += self.weight
    
MAX_APPLES = 1000
MAX_WEIGHT = 300.0
apples = []

# Create apples until the limitations are exceeded
while Apple.total_apples < MAX_APPLES and Apple.total_weight < MAX_WEIGHT:
    apple = Apple()
    apples.append(apple)

# Print the results
print(f'Number of apples processed: {Apple.total_apples}')
print(f'Total weight of apples processed: {Apple.total_weight:.2f} units')


