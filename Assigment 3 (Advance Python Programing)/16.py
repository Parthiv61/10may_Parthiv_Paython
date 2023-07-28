"""Can one block of except statements handle multiple exception?"""

#Yes, a single block of except statements in Python can handle multiple exceptions. This feature allows you to group exception types together and handle them in the same way, reducing code duplication and making your exception handling more concise.

#To handle multiple exceptions in a single except block, you can list the exception types within parentheses, separated by commas. Here's the syntax

try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except (ValueError, ZeroDivisionError):
    print("Invalid input or cannot divide by zero.")
finally:
    print("This block is always executed.")


