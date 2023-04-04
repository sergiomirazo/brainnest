"""
    Write a program to prompt
    the user for hours and rate
    per hour to compute gross pay
"""

hours = float(input("Enter the hours: "))
rate = float(input("Enter your rate: "))
pay = hours*rate
print(f"You must pay: {pay}")
