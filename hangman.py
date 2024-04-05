from wonderwords import RandomWord
import time
random = RandomWord()

tic=time.perf_counter()

def main():
    newWord = ''
    wrongGuesses = []
    guessStatus = []
    answer = generateWord(newWord)
    lives = len(answer) + 2
    answerLetters = list(answer)    
    #print(answerLetters)         -- SEE ANSWER       
    guessStatus += ("_"*len(answer))
    print("\n--------------------------------------------")
    print(f"Let's play HANGMAN! The word has {len(answer)} letters.")
    print("--------------------------------------------")
    
    #Play time counter
    toc=time.perf_counter()
    print(f"You have been playing for {toc - tic:0.0f} seconds\n")

    while guessStatus != answerLetters and lives != 0:
        ltrGuessed = input("Guess a letter: ").upper()
        while ltrGuessed.isalpha() == False or len(ltrGuessed) > 1:
            # printGuesses(guessStatus, wrongGuesses, lives)
            print("\n        ######         Invalid input!       ######\n")
            ltrGuessed = input("      Please enter a single letter: ").upper()
        (guessStatus, wrongGuesses, lives) = checkGuess(ltrGuessed, guessStatus, answerLetters, wrongGuesses, lives)
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
    restart = input(f"\n The word was \"{addSpaces(answerLetters)}\"   |   Play again?  (enter 'Y' to continue, or press 'Enter' to exit)  ").lower()
    if restart == 'y':
        main()

def checkGuess(ltrGuessed, guessStatus, answerLetters, wrongGuesses, lives):
    guessStatus = guessStatus
    ltrPositionInGuess = 0
    if ltrGuessed in guessStatus: 
        print(f"\n######    You have already guessed {ltrGuessed.upper()}!    ######")  #checking if ltr already correctly guessed
        printGuesses(guessStatus, wrongGuesses, lives)
    elif ltrGuessed in wrongGuesses:                                #checking if ltr already incorrectly guessed
        print(f"\n######    You have already guessed {ltrGuessed.upper()}!    ######")
        printGuesses(guessStatus, wrongGuesses, lives)
    elif ltrGuessed in answerLetters:                                 #checking if ltr in answer
        while ltrPositionInGuess != len(answerLetters):   #checking every item in length of list of answer's ltrs
            if answerLetters[ltrPositionInGuess] == ltrGuessed: #checking if index of ltr is the ltr guessed
                guessStatus[ltrPositionInGuess] = ltrGuessed #add ltr guessed to Guessed List
            ltrPositionInGuess += 1
            if guessStatus == answerLetters: #if answer completely guessed return to "main() while loop" and end game
                return guessStatus, wrongGuesses, lives
        printGuesses(guessStatus, wrongGuesses, lives)
    else:  # if ltr is not in answer
        wrongGuesses += ltrGuessed  # add ltr to list of incorrectly guessed ltrs
        lives -= 1
        printGuesses(guessStatus, wrongGuesses, lives)
    return guessStatus, wrongGuesses, lives

def printGuesses(guessStatus, wrongGuesses, lives):
    print(f"\nLives left: {lives}    Current guess:  {addSpaces(guessStatus)}")
    print(f"\n                 Letters used:   {addSpaces(wrongGuesses)}\n")

def addSpaces(lettersOfWord):
    wordWithSpaces = ''
    for i in lettersOfWord:
        wordWithSpaces += (str(i) + ' ')
    return wordWithSpaces

def generateWord(newWord):
    newWord = random.word().upper()
    while ' ' in newWord or '-' in newWord:
        print(f'invalid word {newWord} not chosen')
        newWord = random.word()
    return newWord.upper()

main()