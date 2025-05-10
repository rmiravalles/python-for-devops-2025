# Loops are used to iterate over a sequence (like a list or tuple) or to repeat a block of code multiple times.
names = ('Rita', 'Bob', 'Sue')

# The loop below will iterate over the tuple and print each name
# The name variable will take on the value of each element in the tuple
for name in names:
    print(name)

# Using the range() function to create indexes for a tuple
# The range() function generates a sequence of numbers, which can be used to iterate over a sequence
# The loop below will iterate over the range of numbers from 0 to 2 (the length of the tuple - 1)
for index in range(len(names)):
    print(names[index])

# To add the index to the name, we can use an f-string
for index in range(len(names)):
    print(f"{index}: {names[index]}")

# While loops are used to repeat a block of code as long as a condition is true
# The loop below will continue to run as long as the variable count is less than 5
count = 0
while count < 5:
    print(count)
    count += 1  # Increment the count by 1 each time the loop runs
# The loop will print the numbers 0 to 4
# The loop will stop when count is equal to 5

# The break statement is used to exit a loop prematurely
# The loop below will print the numbers 0 to 4, but will stop when count is equal to 3
count = 0
while count < 5:
    if count == 3:
        break  # Exit the loop when count is equal to 3
    print(count)
    count += 1

# The continue statement is used to skip the current iteration of a loop and move on to the next one
# The loop below will print the numbers 0 to 4, but will skip the number 2
count = 0
while count < 5:
    count += 1
    if count == 2:
        continue  # Skip the current iteration when count is equal to 2
    print(count)

