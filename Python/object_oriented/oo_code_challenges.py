# class Letter:
#     def __init__(self, pattern=None):
#         self.pattern = pattern
#
#     def __str__(self):
#         strepresentation = ''
#         for item in self.pattern:
#             if item == ".":
#                 strepresentation += "dot-"
#             elif item == "_":
#                 strepresentation += "dash-"
#             else:
#                 continue
#         result = strepresentation[:-1]
#         return result
#
#
# class S(Letter):
#     def __init__(self):
#         pattern = ['.', '.', '.']
#         super().__init__(pattern)
# s = S()
# print(s)

# class NumString:
#     def __init__(self, value):
#         self.value = str(value)
#
#     def __str__(self):
#          return self.value
#
#     def __int__(self):
#         return int(self.value)
#
#     def __float__(self):
#         return float(self.value)
#
#     def __add__(self, other):
#         if '.' in self.value:
#             return float(self) + other
#         return int(self) + other
#
#     def __radd__(self, other):
#         return self + other
#
#     def __iadd__(self, other):
#         self.value = self + other
#         return self.value
#
#     def __mul__(self, other):
#         if '.' in self.value:
#             return float(self) * other
#         return int(self) * other
#
#     def __rmul__(self, other):
#         return self * other
#
#     def __imul__(self, other):
#         self.value = self * other
#         return self.value

# class Letter:
#     def __init__(self, pattern=None):
#         self.pattern = pattern
#
#     def __str__(self):
#         output = []
#         for blip in self.pattern:
#             if blip == '.':
#                 output.append('dot')
#             else:
#                 output.append('dash')
#         return '-'.join(output)
#
#     def __iter__(self):
#         yield from self.pattern
#
#
# class S(Letter):
#     def __init__(self):
#          pattern = ['.', '.', '.']
#          super().__init__(pattern)
#
# class Double(int):
#     def __new__(*args, **kwargs):
#         retVal = int.__new__(*args, **kwargs)
#         retVal = retVal * 2
#         return retVal
#
# class Triple(int):
#     def __new(*args, **kwargs):
#         return int.__new__(*args, **kwargs) * 3

# class Liar(list):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     def __len__(self):
#         return super().__len__()+1

# class Letter:
#     def __init__(self, pattern=None):
#         self.pattern = pattern
#
#     def __iter__(self):
#         yield from self.pattern
#
#     def __str__(self):
#         output = []
#         for blip in self:
#             if blip == '.':
#                 output.append('dot')
#             else:
#                 output.append('dash')
#         return '-'.join(output)
#
#     @classmethod
#     def from_string(cls, string):
#         translated = []
#         string = string.split("-")
#         for item in string:
#             if item == 'dash':
#                 translated.append("_")
#             else:
#                 translated.append(".")
#         return cls(translated)
#
# class S(Letter):
#     def __init__(self):
#          pattern = ['.', '.', '.']
#          super().__init__(pattern)
#
# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#
#     @property
#     def area(self):
#         return self.width * self.length
#
#     @property
#     def perimeter(self):
#         return self.length * 2 + self.width * 2

# class Product:
#     _price = 0.0
#     tax_rate = 0.12
#
#     def __init__(self, base_price):
#         self._price = base_price
#
#     @property
#     def price(self):
#         return self._price + (self._price * self.tax_rate)
#
#
#     @price.setter
#     def price(self, price):
#         self._price = price
#
# class Board:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.cells = []
#         for y in range(self.height):
#             for x in range(self.width):
#                 self.cells.append((x, y))
#
#     def __iter__(self):
#         yield from self.cells
#
# class TicTacToe(Board):
#     def __init__(self):
#         super().__init__(witdh = 3, height = 3)

# class Song:
#     def __init__(self, artist, title, length):
#         self.artist = artist
#         self.title = title
#         self.length = length
#
#     def __int__(self):
#         return self.length
#
#     def __eq__(self, other):
#         return int(self) == other
#
#     def __ne__(self, other):
#         return not int(self) == other
#
#     def __gt__(self, other):
#         return int(self) > other
#
#     def __lt__(self, other):
#         return int(self) < other
#
#     def __ge__(self, other):
#         return int(self) > other or int(self) == other
#
#     def __le__(self, other):
#         return int(self) < other or int(self) == other
#
# import random
#
#
# class Die:
#     def __init__(self, sides=2):
#         if sides < 2:
#             raise ValueError("Can't have fewer than two sides")
#         self.sides = sides
#         self.value = random.randint(1, sides)
#
#     def __int__(self):
#         return self.value
#
#     def __add__(self, other):
#         return int(self) + other
#
#     def __radd__(self, other):
#         return self + other
#
# class D20(Die):
#     def __init__(self):
#         super().__init__(sides = 20)
#
#
# class Hand(list):
#     @property
#     def total(self):
#         return sum(self)
#
#     def roll(number = 0):
#         hand = Hand()
#         for _ in range(number):
#             die = D20()
#             print(die.value)
#             hand.append(die)
#         return hand
#
#
# test = Hand.roll(2)
# print(test)
# print(test.total)

# class YatzyScoresheet:
#     def score_ones(self, hand):
#         return sum(hand.ones)
#
#     def _score_set(self, hand, set_size):
#         scores = [0]
#         for worth, count in hand._sets.items():
#             if count == set_size:
#                 scores.append(worth*set_size)
#         return max(scores)
#
#     def score_one_pair(self, hand):
#         return self._score_set(hand, 2)
#
#     def score_chance(self, hand):
#         return sum(hand)
#
#     def score_yatzy(self, hand):
#         count = 0
#         die1 = hand[0]
#         for die in hand:
#             if die == die1:
#                 count += 1
#         if count == 5:
#             return 50
#         return 0

class Die:
    def __init__(self, sides=2):
        if sides < 2:
            raise ValueError("Can't have fewer than two sides")
        self.sides = sides
        self.value = random.randint(1, sides)

    def __int__(self):
        return self.value

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return self + other

class D6(Die):
    def __init__(self):
        super().__init__(sides = 6)

class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super().__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()

    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice


class CapitalismHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size = 2, die_class = D6, *args, **kwargs)

    @classmethod
    def reroll(cls):
        return cls

    @property
    def doubles(self):
        return self[0] == self[1]

    @property
    def ones(self):
        return self._by_value(1)

    @property
    def twos(self):
        return self._by_value(2)

    @property
    def threes(self):
        return self._by_value(3)

    @property
    def fours(self):
        return self._by_value(4)

    @property
    def fives(self):
        return self._by_value(5)

    @property
    def sixes(self):
        return self._by_value(6)

    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }
