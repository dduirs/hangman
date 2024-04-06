# Hangman - for Python CLI
# Copyright (C) 2024 David Duirs
# Originally coded in mid-summer 2023 (northen hemisphere). 
# Refactored in April 2024 while reading Clean Code by Robert C. Martin.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from wonderwords import RandomWord
import time
random = RandomWord()
tic=time.perf_counter() # initiates the timer (while you'll be tempted to play all day, don't forget to go outside!)

def main():    
    newWord = ''
    guessStatus = []
    wrongGuesses = []    
    answerLetters = []
    lives = 0
    ltrGuessed = ''
    (guessStatus, answerLetters, lives) = startNewGame(ltrGuessed, guessStatus, wrongGuesses, answerLetters, lives)
    while isGameOver(guessStatus, answerLetters, lives) == False:
        ltrGuessed = getInput()
        while isGuessValid(ltrGuessed, guessStatus, wrongGuesses) == False:
            ltrGuessed = getInput()
        (guessStatus, wrongGuesses, lives) = checkCurrentGuessAndUpdate(ltrGuessed, guessStatus, answerLetters, wrongGuesses, lives)
        printGuesses(guessStatus, wrongGuesses, lives)
    displayGameResult(lives)
    printTimePlayed()
    playAgain(answerLetters)
    
def startNewGame(ltrGuessed, guessStatus, wrongGuesses, answerLetters, lives):
    answer = generateWord()
    lives = len(answer) + 2
    answerLetters = list(answer)    
    # print(answerLetters)         <-- uncomment to SEE ANSWER for testing purposes     
    guessStatus = []
    guessStatus += ("_"*len(answer))
    print("\n--------------------------------------------")
    print(f"Let's play HANGMAN! The word has {len(answer)} letters.")
    print("--------------------------------------------")
    return guessStatus, answerLetters, lives

def generateWord():
    newWord = random.word()
    while ' ' in newWord or '-' in newWord:
        print(f'invalid word {newWord} not chosen')
        newWord = random.word()
    return newWord.upper()

def isGameOver(guessStatus, answerLetters, lives):
    if guessStatus != answerLetters and lives != 0:
        return False

def getInput():
    ltrGuessed = ''
    ltrGuessed = input("Guess a letter: ").upper()
    return ltrGuessed

def isGuessValid(ltrGuessed, guessStatus, wrongGuesses):
    if ltrGuessed.isalpha() == False or len(ltrGuessed) > 1:
        print("\n        ######         Invalid guess!       ######")
        print("\n                       Please enter a single letter!")
        return False
    elif ltrGuessed in guessStatus or ltrGuessed in wrongGuesses:
        print(f"\n######    You've already guessed {ltrGuessed.upper()}!    ######\n")
        return False
    else:
        return True

def checkCurrentGuessAndUpdate(ltrGuessed, guessStatus, answerLetters, wrongGuesses, lives):
    if ltrGuessed in answerLetters:
        updateCorrectGuesses(ltrGuessed, answerLetters, guessStatus)
    else:
        wrongGuesses += ltrGuessed
        lives = lives-1
    return guessStatus, wrongGuesses, lives

def updateCorrectGuesses(ltrGuessed, answerLetters, guessStatus):
    ltrPositionInGuess = 0
    while ltrPositionInGuess != len(answerLetters):
        if answerLetters[ltrPositionInGuess] == ltrGuessed:
            guessStatus[ltrPositionInGuess] = ltrGuessed
        ltrPositionInGuess += 1
    return guessStatus

def printGuesses(guessStatus, wrongGuesses, lives):
    print(f"\nLives left: {lives}    Current guess:  {addSpaces(guessStatus)}")
    print(f"\n                  Letters used:  {addSpaces(wrongGuesses)}\n")

def addSpaces(lettersOfWord):
    wordWithSpaces = ''
    for i in lettersOfWord:
        wordWithSpaces += (str(i) + ' ')
    return wordWithSpaces
    
def displayGameResult(lives):
    if lives == 0:
        print(f"\n  YOU GOT HUNG!             _________     ")
        print(f"                            |        |      ")
        print(f"                            |        ☹     ")
        print(f"                            |      / | \    ")
        print(f"                            |       / \     ")
        print(f"                            |               ")
        print(f"                          _____             ")
    else: 
        print(f"\n        ๋࣭  ࣪ ˖❇ ๋࣭  ࣪ ˖⊹ ࣪ ˖   YOU WON!  ˖⊹ ࣪ ˖๋࣭  ࣪ ˖❇ ๋࣭  ࣪ ")
        print(f"\n               _________     ")
        print(f"               |        |      ")
        print(f"               |               ")
        print(f"               |             I'm outta here!")
        print(f"               |                  ╰  ☻ /    ")
        print(f"               |                   / |      ")
        print(f"             _____                  / \     ")

def printTimePlayed():
    toc=time.perf_counter()
    print(f"\nYou've been playing for {toc - tic:0.0f} seconds\n")
    
def playAgain(answerLetters):
    restart = input(f"The word was \"{addSpaces(answerLetters)}\"   |   Play again?  (enter 'Y' to continue, or press 'Enter' to exit)  ").lower()
    if restart == 'y':
        guessStatus = []
        main()

main()
