class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property <<---getter
    def radius(self):
        return self.diameter / 2

    @radius.setter <<---setter
    def radius(self, radius):
        self.diameter = radius * 2

small = Circle(10)
print(small.diameter)
# print(small.radius) <<--parentheses not required
# small.radius = 10 <<--CANNOT DO until there is a setter
