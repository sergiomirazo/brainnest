"""
    Brainnest Python Training, Group A | Week 1 | Assignment 1
    Program: palindrome_detector.py
    Author: Sergio Mirazo
    Date: APR / 05 / 2023
"""
resp = True
n = 1
data = []

def attempt():
    global n
    word = input("Attempt number "+str(n)+": ")
    return word

print("Please, enter a palindrome"+
          '\n'+'if you enter a no palindrome'+
          '\n'+'you loose'+'\n'+
          '_________________________________')
while resp:
    word = attempt()
    txt = list(word)
    txt2 = list(word)
    txt2.reverse()
    if txt == txt2:
        print('Palindrome detected +1')
        n += 1
        data.append(word)
    else:
        print('No palindrome, game over...')
        if not data:
            print('No palindrome detected :(')
        else:
            n = n - 1
            print(f'You have entered {n} palindromes')
            print(data)
        resp = False
