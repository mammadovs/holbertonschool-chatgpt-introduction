#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
        Recursively calculates the factorial of a given non-negative integer.
        Factorial of n (n!) is the product of all positive integers up to n.
        By definition, factorial of 0 is 1.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Return Value:
        int: The factorial of the given integer n.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n-1)  # Recursive case: n * factorial of (n-1)

# Get the first command-line argument, convert it to an integer,
# calculate its factorial and store the result in variable 'f'
f = factorial(int(sys.argv[1]))

# Print the calculated factorial to the console
print(f)
