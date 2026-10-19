#Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
#b. 1!+ 2! + 3! + 4!+..... + n!
#c. 1^1 + 2^2 + 3^3+ ...... n^n

import math


def series_a(n):
    return sum(range(1, n + 1))


def series_b(n):
    return sum(math.factorial(i) for i in range(1, n + 1))


def series_c(n):
    return sum(i**i for i in range(1, n + 1))


n = int(input("Enter value of n: "))

print(f"\nResults for n = {n}:")
print(f"a. 1 + 2 + ... + {n} = {series_a(n)}")
print(f"b. 1! + 2! + ... + {n}! = {series_b(n)}")
print(f"c. 1^1 + 2^2 + ... + {n}^{n} = {series_c(n)}")
