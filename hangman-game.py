#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:54:52 2021

@author: williammcintyre
"""

# Hangman Game
# Will McIntyre
# February 8th, 2021

import random

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
      
# Get word bank, split by space to make it into a list!
words = "grandmother reject bundle major cheat pluck structure landowner intermediate dump absorption game pepper humanity indoor".split()

def getRandomWord(wordList):
    # This function returns a random string from the word list
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    # Print hangman pictures based on how many missed letters there are
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    
    # Print missed letters to user
    print("Missed letters: ", end = "")
    for letter in missedLetters:
        print(letter, end = " ")
    print()
    
    # Determine blanks based on number of letters in the secret word
    blanks = "_" * len(secretWord)
    
    for i in range (len(secretWord)):
        # If the secret word letter is in the correct letters guessed, adjust the blanks with filled in correct letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    
    # Print out adjusted blank (if adjusted)
    for letter in blanks:
        print(letter, end= " ")
    print()
    
def getGuess(alreadyGuessed):
    while(True):
        # Get guess input from user, make lowercase
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        
        # Check validity of guess
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("Please enter a new letter.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER.")
        
        # If valid, return the user's guess
        else:
            return guess
        
def playAgain():
    print("Do you want to play again? (yes or no)")
    # Returns True if all of these characteristics are follwoed. Lowercase, starts with 'y'
    return input().lower().startswith('y')

# Main Code
print("H A N G M A N")

# Start missed letters, correct letters at blank, and determine the secret word. The game is not done so it is False.
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameIsDone = False

while(True):
    # Display the board to user
    displayBoard(missedLetters, correctLetters, secretWord)
    
    # Get guess from user
    guess = getGuess(missedLetters + correctLetters)
    
    # If the user's letter guess is in the secret word, add to correct letters, and see if player has won
    if guess in secretWord:
        correctLetters = correctLetters + guess
        
        # Check if player has won
        foundAllLetters = True
        for i in range (len(secretWord)):
            
            # If there is a single character that is in the secret word and not in the correct letters, then user has not found all letters and break
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            
            # If they have found all letters, tell user that they won and indicate that the game is done
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '" You have Won!')
            gameIsDone = True
    
    # If the user's letter guess is not in the secret word, add to missed letters and see if player has lost
    else:
        missedLetters = missedLetters + guess
        
        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            # Display updated board to user, tell that they lost and indicate that it is the end of the game
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
           
    # If gameIsDone comes back as true, then reset all values to blank and get a new word. If gameIsDone comes back as false, break infinite loop and end game.
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
