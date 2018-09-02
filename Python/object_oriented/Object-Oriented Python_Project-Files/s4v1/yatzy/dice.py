import random

class Die:
    def __init__(self, dieSides = 2, dieValue = 0):
        if not dieSides >-2:
            raise ValueError("Must have at least 2 sides")
        if not isinstance(dieSides, int):
            raise ValueError("Sides must be a whole number")
        self.dieValue = dieValue or random.randint(1, dieSides)

class D6(Die):
    def __init__(self, d6Value = 0):
        # no point in having an option to set the sides
        super().__init__(dieSides = 6, dieValue = d6Value)


myDie = Die(dieSides = 4).dieValue
print(myDie)

myDie2 = D6()
