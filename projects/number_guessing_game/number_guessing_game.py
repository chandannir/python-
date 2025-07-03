import random

secretNumber = random.randint(1,100)

while True:
    try:
        choice = int(input("Guess a number between 1 - 100: "))
        if choice > secretNumber:
            print("Too High!")
        elif choice < secretNumber:
            print("Too Low")
        else: 
            print("Congratulations! You guessed the Number")
            break 
        
    except ValueError:
        print("Please enter a Number!")