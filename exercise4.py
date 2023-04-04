"""
    Rewrite your pay computation to give
    the employee 1.5 times the hourly rate
    for hours worked above 40 hours
    0 - 40 : 400
    41 - 45: 75
"""
hours = input("Enter the hours: ")
rate = float(input("Enter your rate: "))
if int(hours)>40:
    pay = float(hours)*rate*1.5
else:
    pay = float(hours)*rate
print(f"You worked {hours}, then your paid is: {pay}")
