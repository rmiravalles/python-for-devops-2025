# F-Strings

F-strings, or formatted string literals, are a way to embed expressions inside string literals, using curly braces `{}`. They were introduced in Python 3.6 and provide a more readable and concise way to format strings compared to the older `%` formatting and `str.format()` methods.
F-strings are prefixed with the letter `f` or `F` before the opening quotation mark. Here's a simple example:

```python
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)
```
This will output:

```
Hello, my name is Alice and I am 30 years old.
```
F-strings can also include expressions, not just variable names. For example:

```python
x = 5
y = 10
result = f"The sum of {x} and {y} is {x + y}."
print(result)
```
This will output:

```
The sum of 5 and 10 is 15.
```
F-strings also support formatting options, similar to the `str.format()` method. For example, you can format numbers, dates, and other types of data:

```python
import datetime
today = datetime.datetime.now()
formatted_date = f"Today's date is {today:%Y-%m-%d}."
print(formatted_date)
```
This will output:

```
Today's date is 2023-10-01.
```

F-strings are evaluated at runtime, which means you can use them in any context where a string is expected. They are also more efficient than the older formatting methods because they are evaluated at runtime and do not require additional function calls.
F-strings are a powerful and flexible way to format strings in Python, making your code more readable and easier to maintain.