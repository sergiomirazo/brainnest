"""
    Brainnest Python Training, Group A | Week 1 | Assignment 1 
    Program: old_checker
    Author: Sergio Mirazo
    Date: APR / 05 / 2023
"""
try:
    age = int(input("Please, enter your age: "))
except ValueError:
    print("Please, enter a valid integer")
    age = int(input("Please, enter your age: "))
if age >= 18:
    print("You are old enough to vote")
else:
    print("You are not old enough to vote")
