"""
    This was my first attempt without cheating or using AI to create a guessing game.
    06/01/2025 22:45

    Bearing in mind that I have not touched python in a very long time as I have
    been busy with work and other things in my personal life.

"""
import random

# Generate a random number between 1 and 9
def randomnum():
    randnum = random.randrange(1, 10)
    return randnum

# Main Code
def run():
    num = randomnum()
    lives = 3
    while(lives >= 0):
        guess = int(input("Enter your guess: "))
        if(guess == num):
            print("You have guessed the answer!")
            return False
        else:
            print(f"This guess is incorrect, please try again! (You have {lives} remaining)")
            #print(f"Debug: {num}")
            lives -= 1
    print("You are out of lives. game over!")
    return False

if __name__ == "__main__":
    run()
