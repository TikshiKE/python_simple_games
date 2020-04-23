###hangman game with pool of words

import time
import random

wordList = ['cat','word','game','spring','plate','sun','girl','table','iron','puke','crowd','song','city','lighter','leg','rock','stick']
startVarY = ['y','yes']
startVarN = ['n','no']

def gameGreetings():
    print('Hello, user! I see you came here to play a guessing game with me and save Mr.Stickman.')
    time.sleep(3)
    print('Very well. But remember...')
    time.sleep(3)
    print('If you\'ll fail I\'ll hang him. (:')
    time.sleep(3)
    gameStart()

def gameStart():
    start = input('Ready to start? (Y/N)').lower().strip()
    time.sleep(1)
    if start in startVarY:
        main()
    elif start in startVarN:
        print('Well, maybe next time.')
        time.sleep(2)
        print('(:')
        time.sleep(1)
    else:
        print('I want to hear strickt answer, yes or no! (Please give propper input)')
        time.sleep(2)
        gameStart()

def main():
    print('I\'ve already chosen the word. Let\'s get started.')
    failCounter = 0
    pickedWordList = list(random.choice(wordList))
    wordField = ['_' for x in pickedWordList]
    print(wordField)
    running = True
    tryedLetters = []
    
    while running:
        
        if wordField == pickedWordList:
            
            print('Congrats, you won!')
            running = False
            
        elif failCounter < 5:
            
            printGallows(failCounter)
            answer = input('So, what\'s your guess? (enter one letter)').lower().strip()
            if answer in pickedWordList:
                
                index = pickedWordList.index(answer)
                wordField[index] = answer
                print('______________________________________')
                print('Nice one! There is a letter like this!')
                tryedLetters.append(answer)
                print('You already tried:')
                print(tryedLetters)
                print('The gessing word is:')
                print(wordField)
                
            else:
                time.sleep(1)
                print('______________________________________')
                print('Oops, wrong guess.')
                tryedLetters.append(answer)
                print('You already tried:')
                print(tryedLetters)
                print('The gessing word is:')
                print(wordField)
                failCounter += 1
                
        elif failCounter == 5:
            
            printGallows(failCounter)
            print('Sorry, Mr.Stickman is dead.')
            running = False
            anotherTry = input('Reset and start over? (Y/N)').lower().strip()
            
            if anotherTry in startVarY:
                gameStart()
            else:
                print('Since this is not a Yes, I stop the game.')


def printGallows(failCounter):
    if failCounter == 0:
        print('  _________')
        print('  |/')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('__|_________')
        print('|          |')
    elif failCounter == 1:
        print('Legs appeared')
        print('  _________')
        print('  |/ ')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('  |    / \ ')
        print('  |   /   \ ')
        print('__|_________')
        print('|          |')
    elif failCounter == 2:
        print('Body appeared')
        print('  _________')
        print('  |/')
        print('  |')
        print('  |     |')
        print('  |     |')
        print('  |     |')
        print('  |    / \ ')
        print('  |   /   \ ')
        print('__|_________')
        print('|          |')
    elif failCounter == 3:
        print('Right arm appeared.')
        print('  _________')
        print('  |/')
        print('  |')
        print('  |    _|')
        print('  |   / |')
        print('  |     |')
        print('  |    / \ ')
        print('  |   /   \ ')
        print('__|_________')
        print('|          |')
    elif failCounter == 4:
        print('Left arm appeared. Last chance!')
        print('  _________')
        print('  |/ ')
        print('  |')
        print('  |    _|_')
        print('  |   / | \ ')
        print('  |     |')
        print('  |    / \ ')
        print('  |   /   \ ')
        print('__|_________')
        print('|          |')
    elif failCounter == 5:
        print('This is the end.')
        print('  _________')
        print('  |/    |')
        print('  |   (o_o)')
        print('  |    _|_')
        print('  |   / | \ ')
        print('  |     |')
        print('  |    / \ ')
        print('  |   /   \ ')
        print('__|_________')
        print('|          |')

gameGreetings()
