#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) < 2:
    print("Usage: python3 script.py <non-negative integer>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 0:
        print("Error: factorial is not defined for negative numbers")
        sys.exit(1)
except ValueError:
    print("Error: input must be an integer")
    sys.exit(1)

f = factorial(n)
print(f)
