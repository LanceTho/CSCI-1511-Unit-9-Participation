"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 

Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
import random
class Die:

    def __init__(self, __sides: int = 6) -> None:
        self.__sides: int = __sides
    
    def roll_dice(self) -> int:
        return random.randint(0,self.__sides)
    
die_6: Die = Die()
print("Rolling 6-sided die 10 times")
for i in range(10):
    print(f"{die_6.roll_dice()}")

die_10: Die = Die(10)
print("Rolling 10-sided die 10 times")
for i in range(10):
    print(f"{die_10.roll_dice()}")

die_20: Die = Die(20)
print("Rolling 20-sided die 10 times")
for i in range(10):
    print(f"{die_20.roll_dice()}")