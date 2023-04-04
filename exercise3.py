"""
    Write a program wich prompts the user
    for a Celsius temperature, convert the
    temperature to Fahrenheit, and print out
    the converted temperature
"""
temp = float(input("Enter the current temperature in °C: "))
F = lambda C: 1.8*C+32
print("The current temperature is "+str(F(temp))+" °F")
