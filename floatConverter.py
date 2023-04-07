"""
    Brainnest Python Training, Group A | Week 1 | Assignment 1
    Error Handling 
    Program: floatConverter.py
    Author: Sergio Mirazo
    Date: APR / 06 / 2023
"""
data = ['6', '7', '8', '9', '10', 'Awesome', '5.6']
print("You have the next data list entry: ")
print(data)
print("________________________________________________")

def float_converter(data):
    storage = []
    for i in range(0,len(data)):
        print(f"converting the {i} element to float")
        try:
            num = float(data[i])
            storage.append(num)
        except ValueError:
            num = input("Please, enter a valid number: ")
            num = float(num)
            storage.append(num)
    return storage

converted = float_converter(data)
print("Converted data to float format: ")
print(converted)
