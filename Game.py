import random as rm
import time

#Game class
class Game:
    def playing(self, difficulty, chances):
        print(f"Great! You have selected the {difficulty} difficulty level.")
        print("Let's start the game!")
        print("I'm thinking of a number between 1 and 100.")
        print(f"You have {chances} chances to guess the correct number.")
        continuing = True
        winning = False
        number = rm.randint(1,100)
        counter = 1
        hint = chances // 2
        while continuing:
            print("Enter your guess: ")
            answer = int(input())
            if continuing and counter >= hint:
                diff = abs(answer-number)
                if number < answer and diff < 10:
                    print("You're pretty close!! Just a little bit less...")
                elif number > answer and diff < 10:
                    print("You're pretty close!! Just a little more perhaps?")
                elif diff > 20:
                    print("You're too far... like, more than 20 numbers away...")
            if answer == number:
                continuing = False
                winning = True
                break
            else:
                counter += 1
                if answer > number:
                    print(f"Incorrect! The number is less than {answer}")
                else:
                    print(f"Incorrect! The number is more than {answer}")
                
                if counter > chances:
                    continuing = False
        if not continuing and winning:
            print(f"Congratulations! You guessed the correct number in {counter} attempts.")
        if not continuing and not winning:
            print("You have no more chances! Sorry, you lost.")
            print(f"The correct number was {number}")

#The timer
def decorTime(original):
    def funcionDec():
        start = time.time()
        original()
        fin = time.time()
        secs_original = fin - start
        secs = int(secs_original)
        if secs > 60:
            mins = secs // 60 
            mins = int(mins)
            if mins < 10:
                mins = f"0{mins}"
            secs = secs % 60
        else:
            mins = "00"
        if secs < 10:
            secs = f"0{secs}"
        print(f"Your timing trying to guess: {mins}:{secs}")
    return funcionDec

#Difficulties
game = Game()
@decorTime
def easy_difficulty():
    game.playing("Easy", 10)

@decorTime
def medium_difficulty():
    game.playing("Medium", 5)

@decorTime
def hard_difficulty():
    game.playing("Hard", 3)

#Game
keep_playing = True
while keep_playing:
    print("Welcome to the Number Guessing Game!")
    print('''Please select the difficulty level:
        1. Easy (10 chances)
        2. Medium (5 chances)
        3. Hard (3 chances)''')
    diff = int(input())
    if diff == 1:
        easy_difficulty()
    elif diff == 2:
        medium_difficulty()
    elif diff == 3:
        hard_difficulty()
    else:
        print("I couldn't find a game difficulty, please try again")
        break
    print("""Nice game! Want to play again?
          1. Yes
          2. No""")
    select = int(input())
    if select == 1:
        continue
    elif select == 2:
        print("Goodbye! Hope to see you later.")
        keep_playing = False
    else:
        break