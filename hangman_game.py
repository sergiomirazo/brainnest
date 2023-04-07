'''
program: hangman_game.py
author: Sergio Mirazo
description: The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
date: APR / 06 / 2023
'''
import random as r
words = [
    ['banana', 'apple', 'orange', 'pineapple', 'tomato',
     'watermelon', 'strawberry', 'grape', 'pear', 'peach',
     'cherry', 'lemon', 'lime', 'mango', 'melon', 'coconut',
     'avocado', 'blueberry', 'raspberry', 'blackberry'],
    ['elephant', 'tiger', 'lion', 'giraffe', 'zebra', 'rhino',
     'hippopotamus', 'gorilla', 'monkey', 'panda', 'penguin',
     'kangaroo', 'koala', 'bear', 'wolf', 'fox', 'deer',
     'rabbit', 'mouse', 'rat', 'cat', 'dog', 'cow', 'sheep'],
    ['Schrodinger', 'Newton', 'Einstein',
         'Galileo', 'Copernicus', 'Hubble', 'Kepler',
         'Hawking', 'Planck', 'Euler', 'Fermat',
         'Archimedes', 'Euclid', 'Pascal', 'Pythagoras',
         'Ramanujan', 'Lovelace', 'Curie', 'Bohr', 'Maxwell',
         'Faraday', 'Tesla', 'Franklin', 'Hooke',
         'Hertz', 'Coulomb', 'Ohm', 'Avogadro',
         'Dalton', 'Mendeleev', 'Rutherford', 'Thomson',
         'Raman',
         'Saha', 'Soddy', 'Stoney', 'Wien', 'Boltzmann',
         'Fermi', 'Pauli', 'Dirac']
]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
           'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

body = ['left leg', 'right leg', 'left arm', 'right arm', 'torso', 'head']

n = 1
resp = True

def attempt():
    global n
    word = input("Attempt number "+str(n)+", choose a letter: ")
    n += 1
    return word

print('Welcome to the Hunger games!'+'\n'+'I mean, hangman game!')
difficult = input('Choose a difficulty: easy, medium, hard: ')
match difficult:
    case 'easy':
        words = words[0]
        print('You have to guess the name of a fruit.')
    case 'medium':
        words = words[1]
        print('You have to guess the name of an animal.')
    case 'hard':
        words = words[2]
        print('You have to guess the name of a famous scientist.')

print('You have 6 tries to guess the correct letters.'+
      '\n'+'Good luck!')

print('///////////////////////////////////////////////////////')

word = r.choice(words).lower()
txt = list(word)
txt = set(txt)
storage1 = list(word)
for i in range(len(word)):
    storage1[i] = '___'

while resp:
    paz=input('You have '+str(len(body))+' tries left [press Enter to continue]')
    print('_________________________________________________')
    paz=input('Your options: [press Enter to continue]')
    print(letters)
    print('___________________________________________________')
    print('Guess the word: ')
    print(storage1)
    letter = attempt().lower()
    if letter in word:
        letters.remove(letter)
        for i in range(len(word)):
            if letter == word[i]:
                storage1[i] = letter
        txt.remove(letter)
        if not txt:
            print('CONGRATS! You guessed the word '+word+' !')
            resp = False
    else:
        print(f"Sorry, the letter {letter} is not in the word."+
              '\n'+"You lost a "+body.pop(0))
        
        if not body:
            print('You lost the game!'+
                  '\n'+'The word was '+word)
            resp = False
