# class:
#     attributes
#
# resulting object = instance
# functions defined inside a class = method (the actions that your class can do)
# methods are always used by the instance, not the class
# all methods take at least one argument, which represents the instance (self)
# don't use 'self' in the function itself when called by the instance
# if you called it on the class itself, you'll need a name of an Instance
# Thief.pickpocket(ann)
# ann.pickpocket()
# if within another method, self.pickpocket()
#
# class names start with a captial letter --BestProgrammer
#
# From file import class
#
# You can change attributes in an instance and it won't change the attribues in the class
# Instances can be deleted with del
#
#     def __init__(self, name, sneaky = True, **kwargs):
#         self.name = name
#         self.sneaky = sneaky
#
#         for key, value in kwargs.items():
#             setattr(self, key, value)

#
# When you use super() you have to specify the method name and its arguments
# Subclasses can take different arguments than their parent's class
#     def __init__(self, name, sneaky = True **kwargs):
#         super().__init__(name, **kwargs)
#         self.sneaky = sneaky
# Leave out the parent's self when supering
# if you call multiple inheritance classes, the most dominant class should be placed to the right
# Method Resolution Order
# Make name a keyword argument by setting it to name = "", which will throw an error
#     def __init__(self, name="", **kwargs):
#         if not name:
#             raise ValueError("'name' is required")
#
#
# isinstance('a', str) = True
# issubclass(Thief, Character) = True
# type(kenneth) = <class 'thieves.Thief'>
# kenneth.__class__ = <class 'thieves.Thief'>
# kenneth.__class__.__name__ = 'Thief'
#
#
# magic methods are often called on the main parent class
#
# add method defines a self and other. If the other is a class you
# will need to define the method to account for the other being
# an instance --- this is what the radd method does
#
# iadd is for += situations where the instance of the class is on both
# sides of the +
#
# yeild functions as a return that allows the function to return a value
# but to keep on running.
# for item in self.slots:
#     yield item
# ----->>> yield from self.slots

# if mutable data type, use init
# if immutable data type, use new


# class ReversedStr(str):
#     def __new__(*args, **kwargs): <<--- use for immutable data type
#         self = str.__new__(*args, **kwargs) <<--- replaces 'super' for immutable data type. Super is risky.
#         self = self[::-1]
#         return self

# call dir() on an object to get all the methods it uses

# foo = Die()
# foo.roll()
#
# Die.rollSomeDice()
#
# class Die:
#     def __init__(self):
#         pass
#
#     def roll(self):
#         pass
#
#     def rollSomeDice():
#         return false
#
# from somewhere import Die
#
# Die.roll()
#
# class Die:
#     def roll():
#         return false
#
# foo = Hand()
# foo.sort()
# print foo[0]
# foo.firstCard()
#
# class Hand(list):
#     pass
#     def firstCard(self):
#         return self[0]
