import random
from characters import famous_people

playerScore = 0

print("Hello, welcome to the guessing game! Guess which character has the most Google searches!")

def getCharacter(array):
   return random.choice(array)

startingChar = getCharacter(famous_people)

def getNextChar(currentChar, array):
   filteredChars = [item for item in array if item != currentChar]
   return random.choice(filteredChars)

print(f"The starting character is {startingChar['name']}!")

# Loop di gioco
while True:

    nextChar = getNextChar(startingChar, famous_people)


    print(f"Do you think {startingChar['name']} has more or less Google searches than {nextChar['name']}? (Type 'more' or 'less')")


    userAnswer = input().strip().lower()


    if (userAnswer == "more" and startingChar['google_searches'] > nextChar['google_searches']) or \
       (userAnswer == "less" and startingChar['google_searches'] < nextChar['google_searches']):
        print(f"Correct! {startingChar['name']} had {startingChar['google_searches']} searches, and {nextChar['name']} had {nextChar['google_searches']} searches.")
        playerScore += 1
    else:
        print(f"Incorrect! {startingChar['name']} had {startingChar['google_searches']} searches, and {nextChar['name']} had {nextChar['google_searches']} searches.")
        print(f"Game Over! Your final score is {playerScore}.")
        break 

    startingChar = nextChar
