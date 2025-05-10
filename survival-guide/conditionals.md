# Conditionals in Python

## Control structures

Control structures are used to control the flow of execution in a program. In Python, there are three main types of control structures: sequential, selection, and repetition.

- **Sequential**: The default mode of execution, where statements are executed one after the other.
- **Selection**: Used to make decisions in the code. This is done using `if`, `elif`, and `else` statements.
- **Repetition**: Used to repeat a block of code multiple times. This is done using loops like `for` and `while`.

## If statement

The `if` statement is used to execute a block of code if a certain condition is true. The syntax is as follows:

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

## If-else statement

The `if-else` statement is used to execute one block of code if a condition is true and another block of code if the condition is false. The syntax is as follows:

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
```
## If-elif-else statement

The `if-elif-else` statement is used to check multiple conditions. The syntax is as follows:

```python
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")
```