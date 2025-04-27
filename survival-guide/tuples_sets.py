# Tuples, like lists, are used to store multiple items in a single variable.
# Tuples are immutable, meaning we can't change its values.
# Tuples are written between parenthesis ().
# We can use tuples to store sets of values that should not be changed throughout the life of a program.
# Like lists, we can store any datatype in a tuple.

dimensions = (200, 140)
dimensions[0] = 250  # if we try to modify an element in a tuple, we get an error

# We can, however, assign new values to a tuple. This will redefine the entire tuple.
dimensions = (180, 110)

print(dimensions)

# Sets are unordered collections of unique elements.
# Sets are written with curly brackets {}.
# Sets cannot have duplicate values.

fruit_set = {'apple', 'banana', 'cherry', 'lemon', 'apple', 'kiwi'}

# A set can only contain unique values, so 'apple' will only be added once.
print(fruit_set)

fruit_set.add('orange')  # this will add a new element to the set.
fruit_set.add('banana')  # this will not add a new element to the set, because 'banana' already exists in the set.
fruit_set.remove('banana')  # this will remove 'banana' from the set.