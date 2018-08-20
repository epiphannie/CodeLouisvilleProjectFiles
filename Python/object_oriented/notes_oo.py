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
