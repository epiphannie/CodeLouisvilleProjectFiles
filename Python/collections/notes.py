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

tuples are defined using  = (,). The comma makes the tuple so a one-item tuple needs a comma
tuples are not mutable
dir(item) will give you all the methods you can use on them
you can change items in a list in a tuple because lists are mutable.
Strings and tuples are not

a = 5
b = 2, need to swap them
a, b = b, a unpacking the tuple
tuples unpack into the variables on the left of the equals sign

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total
add(5, 5) >>> 10

def add(base, *args):
    total = base
    for num in args:
        total += num
    return total
add(5, 20) >> 25

arguments, then *args, then **kwargs
