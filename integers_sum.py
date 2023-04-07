"""
    Brainnest Python Training, Group A | Week 1 | Assignment 1 
    Program: integers_sum.py
    Author: Sergio Mirazo
    Date: APR / 05 / 2023
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
        txt = int(attempt(i))
    if integer % 2 == 0:
        data.append(integer)

total = sum(data)
print(f'The sum of the even integers is {total}')
