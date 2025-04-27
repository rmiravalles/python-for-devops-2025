name = "Joe"
age = 132

# string concatenation
# integers must be converted to strings before concatenation.
print("Hello, my name is " + name + " and I am " + str(age) + " years old.")

# str.format() method
# the values are passed as arguments to the format() method.
# Automatically handles type conversion (e.g., age doesn't need to be explicitly converted to a string).
print("Hello, my name is {} and I am {} years old.".format(name, age))

# The f-string method is the most efficient way to format strings in Python 3.6 and later.
# It is also the most readable and the most flexible.
print(f"Hello, my name is {name} and I am {age} years old.")