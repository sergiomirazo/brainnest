"""
    Brainnest Python Training, Group A | Week 1 | Assignment 1
    Error Handling 
    Program: biggest_integer.py
    Author: Sergio Mirazo
    Date: APR / 06 / 2023
"""

data = []

def attempt(i):
    txt = input("Enter number "+str(i)+": ")
    return txt

try:
    n = int(input("How long is your list of integers? "))
except ValueError:
    print("Please, enter a valid integer")
    n = int(input("How long is your list of integers? "))
    
for i in range(1,n+1):
    try:
        integer = int(attempt(i))
    except ValueError:
        print("Please, enter a valid integer")
        integer = int(attempt(i))
    data.append(integer)
res = max(data)
print(f"Numbers list: {data}")
print(f"The biggest integer is: {res}")
