"""
    Brainnest Python Training, Group A | Week 1 | Assignment 1 
    Program: integers_divisibleBy3
    Author: Sergio Mirazo
    Date: APR / 05 / 2023
"""
try:
    n = int(input("Please, enter a integer: "))
except ValueError:
    print("Please, enter a valid integer")
    n = int(input("Please, enter a integer: "))

def prime(n):
    res = True
    if n < 2:
        res = False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res = False
    return res

resp = prime(n)
if resp:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
