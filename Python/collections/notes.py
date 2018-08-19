Lists
# + to append items to a list. Requires brackets. += to completely update the list
# .append to append an item to a list. Will append a literal list if given a list
# # Enter item as string if using append methond, unless you want to append a list.
# .extend requires a list but will only save string values, like += method.
# Can extend anything iterable
#
# a = [1,2,3]
# a.extend("abc")
# a = [1, 2, 3, 'a', 'b', 'c']
#
# .insert lets you add a value at any particular point, using index, like del
#
# lists are mutable and will be changed with each method you run on them
#
# .remove removes the first instance of that value in the list
#
# # slices exlcude the index at the end.
# Always returns the type of data that it is created from
# Will slice past the last index in the list
# slice[:]will get you back a copy of your entire list
# slice: start:stop:step default to 1
# Can apply to anything interable
    # can reverse a list by stepping back with -1

tuples
# tuples are defined using  = (,). The comma makes the tuple so a one-item tuple needs a comma
# tuples are not mutable
# dir(item) will give you all the methods you can use on them
# you can change items in a list in a tuple because lists are mutable.
# Strings and tuples are not
#
# a = 5
# b = 2, need to swap them
# a, b = b, a unpacking the tuple
# tuples unpack into the variables on the left of the equals sign
#
# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# add(5, 5) >>> 10
#
# def add(base, *args):
#     total = base
#     for num in args:
#         total += num
#     return total
# add(5, 20) >> 25
#
# arguments, then *args, then **kwargs

# list(enumerate("abc"))
# [(0, 'a'), (1, 'b'), (2, 'c')]
# creates a tuple using index and the next value
#
# for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
#     print("{}: {}".format(index + 1, letter))
# workds the same as a count = 1, for letter in alphabet, count +=1
# Can take a second argument, start = for the starting value

# sets
# https://docs.python.org/3/library/stdtypes.html#set
# a set is a collection of anything. Each thing can only be in the set onceself.
# They are iterable, each item must be unique, they do not have indexes
# Can be created with curly bracess.
# If you make a blank one, it has to be made with set()
# Python sorts the set in a way that makes sense to python
# .add() to adding
# .update() will add an entire set to the set. Many sets can be added at once
# .remove() enter value to be removed, there's only one! Will throw an error if not present
# .discard() if the value can be removed, it will be, otherwise no error
# .pop() to remove last value and save it if need be
#
# union shows all the distinct elements present in both sets (order not important)
# difference is everything in the first set but not the second
# symmetric difference is everything that's unique to either set (order not important)
# intersection is all items in both sets, but no duplicates
# set1.union(set2) THIS DOES NOT CHANCE SET1, you can also use a |. Set1 | Set2
# set1.difference(set2) <> set2.difference(set1), you can also use a -
# set2.symmetric_difference(set1), set1 ^ set2
# set1.intersection(set2), set1 & set2
