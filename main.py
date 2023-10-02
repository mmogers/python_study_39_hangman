import random, os, time

listOfWords = ["british", "computer", "grave", "accent", "past", "genius", "wall", "apple", "tree", "household"]
myWord = random.choice(listOfWords).lower()
print(f"myWord = {myWord}\n")

myWordLength = len(myWord) 
lifeCount = 7
guessedLetters = 0
word = []
#initializing a word array with "_"
for index in range (myWordLength):
  word.append("_")
print(f"word = {word}")

#how many time the letter appears in the word
def howManyTimes (letter, myWord):
  count = 0
  if letter in myWord: 
    for index in range (myWordLength):
      if letter == myWord[index]:
        count += 1
    return count  
  else:
    return 0

#printw the guessed word with default unguessed "_"
def printWord():
  print()
  for index in range (myWordLength):
    print(word[index], end = " ")
  print()

#finds a next free index of the letter, if no free index returns -1
def findFreeIndex(letter, times):
  while times > 0:
    for index in range (myWordLength):
      if word[index] == "_" and myWord[index] == letter:
        times -= 1
        return int(index)
    return -1

#prints hangman for every of six attempts
def printHangman(number):
  if number == 6:
    print("  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========")
  elif number == 5:
    print("  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========")
  elif number == 4:
    print("  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========")
  elif number == 3:
    print("  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========")
  elif number == 2:
    print("  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========")
  elif number == 1:
    print("  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========")
  elif number == 0:
    print("  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========")
  time.sleep(2)

#prints in sinle for one or plural for lives left
def printLivesLeft():
  if lifeCount != 1:
    print(f"\nYou have {lifeCount} lives left") 
  else:
    print(f"\nYou have {lifeCount} life left") 
#---------------------------------------------------------------------
while guessedLetters < myWordLength and lifeCount > 0:
  time.sleep(1)
  os.system("clear")
  printWord()
  myLetter = input("\nChoose a letter: ").lower()
  times = howManyTimes(myLetter, myWord) #how many times appears the letter in the word
  if times == 0: 
    lifeCount -= 1 #a bad guess
    print("\nNope, not in there!")
    printWord()
    if lifeCount > 0:
      printHangman(lifeCount)
      printLivesLeft()
    else: 
      printHangman(lifeCount)
      time.sleep(2)
      break
  else:    
    print("You found a letter!")
    while times > 0 : 
      index = findFreeIndex(myLetter, times) #index- the index of the letter in word array
      if index != -1:
        word[index] = myLetter
        times -= 1
        guessedLetters += 1
        if guessedLetters == myWordLength:
            break
      else: #index = -1 - no free indes - the letter was guessed before
        print("But you've tried that before!")
        lifeCount -= 1
        printLivesLeft() 
        printHangman(lifeCount)
        time.sleep(1)
        break
    time.sleep(1)
    os.system("clear")
    printWord()
    #time.sleep(1)
if lifeCount == 0: #no more attempts
  os.system("clear")
  print(f"You've lost the game !, the word was - {myWord}")
  printHangman(lifeCount)
elif guessedLetters == myWordLength: #all the letters of the word were guessed
  os.system("clear")
  printWord()
  if lifeCount != 1:
    print(f"\nYou won with  {lifeCount} lives left") 
  else:
    print(f"\nYou won with {lifeCount} life left") 