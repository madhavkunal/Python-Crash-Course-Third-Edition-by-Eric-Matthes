# Exercise 9 - 13 (Dice)

from random import randint  # import random integer class method from random module

"""Create class for Die instantiation"""

class Die:  
    def __init__(self, num_sides=6):    # By default, an instance is  a 6-sided die
        self.num_sides = num_sides  # The number of sides can be customized based on the instance
        print(f"\n\tThis dice has {self.num_sides} sides\n")    

    def roll_die(self): # Give die a roll function
        self.roll = randint(1, self.num_sides)  # use randint class method that we imported earlier to give a random number
        # emulating the possible numbers it could hit based on the range or number of sides for a die instance
        print(f"\tYou rolled a {self.roll}!")

# Create a 6-sided die and roll it ten times
six_sided_die = Die()   # Instantiate a 6 sided-die (leave arguments blank since die has 6 sides by default)
for _ in range(10): # For up to 10 times
    six_sided_die.roll_die()    # Roll the dice

# Create a 10-sided die and roll it ten times
ten_sided_die = Die(10) # Instantiate a 10 sided-die
for _ in range(10): # For up to 10 times
    ten_sided_die.roll_die()   # Roll the dice

# Create a 20-sided die and roll it ten times
twenty_sided_die = Die(20)  # Instantiate a 20 sided-die
for _ in range(10): # For up to 10 times
    twenty_sided_die.roll_die()   # Roll the dice

print()