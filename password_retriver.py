"""
    Brainnest Python Training, Group A | Week 1 | Assignment 1
    Error Handling 
    Program: password_retriver.py
    Author: Sergio Mirazo
    Date: APR / 06 / 2023
"""

users_vip = {'Magda':False, 'Robert':True, 'Linda':True,
             'John':False, 'Anna': True, 'Paul': True}
users_email = {'Magda':'magda@gmail.com', 'Robert':'robert@gmail.com', 'Linda':'linda@gmail.com',
             'John':'john-romero@gmail.com', 'Anna': 'mary-ann@gmail.com', 'Paul': 'les-paul@gmail.com'}
users_pass = {'Magda':'aksfnkfa', 'Robert':'32nj5n32', 'Linda':'fk0232rf*',
             'John':'-34321r123d', 'Anna': 'mary-ann', 'Paul': '-sand32i62n+'}

users = [users_vip, users_email, users_pass]
        
def get_email(users):
    try:
        name = input("Select by name: ")
        emails = users[1]
        email = emails[name]
        return email
    except KeyError:
        print("Oh please, enter a valid name")
        name = input("Please, select by name: ")
        emails = users[1]
        email = emails[name]
        return email

def get_pass(users):
    try:
        name = input("Select by name: ")
        var = users[2]
        txt = var[name]
        return txt
    except KeyError:
        print("Oh please, enter a valid name")
        name = input("Please, select by name: ")
        var = users[2]
        txt = var[name]
        return txt
    
def get_vip(users):
    try:
        name = input("Select by name: ")
        var = users[0]
        txt = var[name]
        return txt
    except KeyError:
        print("Oh please, enter a valid name")
        name = input("Please, select by name: ")
        var = users[0]
        txt = var[name]
        return txt

print("Welcome, to palomino's email and password retriever"+
      '\n'+"Please, select an option: "+
      '\n'+"1. Get email"+
      '\n'+"2. Get password"+
      '\n'+"3. Get VIP status")
try:
    resp = int(input("Enter your option: "))
except ValueError:
    print("Please, just enter a number of your option")
    resp = int(input("Enter your option: "))
    
match resp:
    case 1:
        txt = get_email(users)
        print(f'email: {txt}')
    case 2:
        txt = get_pass(users)
        print(f'password: {txt}')
    case 3:
        txt = get_vip(users)
        if txt:
            print(f"User is VIP")
        else:
            print(f"User is not VIP")
