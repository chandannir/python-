import akinator

def play_akinator():
    print("Welcome to Akinator!")
    
    # Initialize Akinator
    aki = akinator.Akinator(language=akinator.Language.from_str('en'), theme=akinator.Theme.from_str('animals'), child_mode=False)

    # Start the game and get the first question
    question = aki.start_game()

    while aki.progression <= 80: # Or another threshold you prefer
        print(f"Question: {question}")
        answer = input("Your answer (yes/no/idk/probably/probably not/back): ").lower()

        if answer == "back":
            try:
                question = aki.back()
            except akinator.CantGoBackAnyFurther:
                print("Can't go back any further.")
        else:
            try:
                question = aki.answer(answer)
            except akinator.InvalidAnswerError: # Corrected exception name based on typical library patterns
                print("Invalid answer. Please use 'yes', 'no', 'idk', 'probably', 'probably not', or 'back'.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break
        
        if aki.progression > 80 : # check after answering
             break


    # Make a guess
    guess = aki.win()

    if guess:
        print(f"\nI think your character is: {guess['name']}")
        print(f"Description: {guess['description']}")
        if guess['absolute_picture_path']:
             print(f"Image: {guess['absolute_picture_path']}")
        
        correct_guess = input("Am I correct? (yes/no): ").lower()
        if correct_guess == "yes":
            print("Yay! I guessed it right.")
        else:
            print("Oops! I'll try to do better next time.")
    else:
        print("I couldn't guess your character. You win!")

if __name__ == "__main__":
    play_akinator()
