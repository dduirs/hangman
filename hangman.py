# Hangman - for Python CLI - Copyright (C) 2024 David Duirs
# Refactored while reading Clean Code by Robert C. Martin.
# This program is free software:
#     you can redistribute it and/or modify it under the terms of the GNU General Public License
#     as published by the Free Software Foundation, either version 3 of the License, or
#     any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
#     without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#     See the GNU General Public License for more details.

from wonderwords import RandomWord
import time
random = RandomWord()
tic=time.perf_counter() # initiates the timer (while you'll be tempted to play all day, don't forget to go outside!)

def main():    
    newWord = ''
    correctGuesses = []
    wrongGuesses = []    
    answerLetters = []
    lives = 0
    ltrGuessed = ''
    (correctGuesses, answerLetters, lives) = startNewGame(correctGuesses, answerLetters, lives)
    while isGameOver(correctGuesses, answerLetters, lives) == False:
        ltrGuessed = getInput()
        while isGuessValid(ltrGuessed, correctGuesses, wrongGuesses) == False:
            ltrGuessed = getInput()
        (correctGuesses, wrongGuesses, lives) = checkGuessAndUpdate(ltrGuessed, correctGuesses, answerLetters, wrongGuesses, lives)
        printGuesses(correctGuesses, wrongGuesses, lives)
    displayGameResult(lives)
    printTimePlayed()
    playAgain(answerLetters)
    
def startNewGame(correctGuesses, answerLetters, lives):
    answer = generateWord()
    lives = len(answer) + 2
    answerLetters = list(answer)
    correctGuesses = []
    correctGuesses += ("_"*len(answer))
    print("\n--------------------------------------------")
    print(f"Let's play HANGMAN! The word has {len(answer)} letters.")
    print("--------------------------------------------")
    return correctGuesses, answerLetters, lives

def generateWord():
    newWord = random.word()
    while ' ' in newWord or '-' in newWord:
        print(f'invalid word {newWord} not chosen')
        newWord = random.word()
    return newWord.upper()

def isGameOver(correctGuesses, answerLetters, lives):
    if correctGuesses != answerLetters and lives != 0:
        return False

def getInput():
    ltrGuessed = ''
    ltrGuessed = input("Guess a letter: ").upper()
    return ltrGuessed

def isGuessValid(ltrGuessed, correctGuesses, wrongGuesses):
    if ltrGuessed.isalpha() == False or len(ltrGuessed) > 1:
        print("\n        ######         Invalid guess!       ######")
        print("\n                       Please enter a single letter!")
        return False
    elif ltrGuessed in correctGuesses or ltrGuessed in wrongGuesses:
        print(f"\n######    You've already guessed {ltrGuessed.upper()}!    ######\n")
        return False
    else:
        return True

def checkGuessAndUpdate(ltrGuessed, correctGuesses, answerLetters, wrongGuesses, lives):
    if ltrGuessed in answerLetters:
        updateGuessStatus(ltrGuessed, answerLetters, correctGuesses)
    else:
        wrongGuesses += ltrGuessed
        lives = lives-1
    return correctGuesses, wrongGuesses, lives

def updateGuessStatus(ltrGuessed, answerLetters, correctGuesses):
    ltrPositionInGuess = 0
    while ltrPositionInGuess != len(answerLetters):
        if answerLetters[ltrPositionInGuess] == ltrGuessed:
            correctGuesses[ltrPositionInGuess] = ltrGuessed
        ltrPositionInGuess += 1
    return correctGuesses

def printGuesses(correctGuesses, wrongGuesses, lives):
    print(f"\nLives left: {lives}    Current guess:  {addSpaces(correctGuesses)}")
    print(f"\n                  Letters used:  {addSpaces(wrongGuesses)}\n")

def addSpaces(lettersOfWord):
    lettersSpaced = ''
    for letter in lettersOfWord:
        lettersSpaced += (str(letter) + ' ')
    return lettersSpaced
    
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
    restart = input(f"The word was \"{addSpaces(answerLetters).rstrip()}\"   |   Play again?  (enter any key to continue, or press 'Enter' to exit)  ").lower()
    if restart != '':
        main()

main()
