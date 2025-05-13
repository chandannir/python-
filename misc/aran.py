import time       # Allows us to add delays (for slow typing effects)
import sys        # Used here only for system level functions (not directly used in this script)
import os         # this import is used to clear the terminal screen

# Function to clear the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # Uses 'cls' for Windows and 'clear' for other OS

# Function to slowly type out input prompts with a delay between characters
def slow_input(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)  # Prints characters one by one
        time.sleep(delay)                # Waits for 'delay' seconds
    print()  # Prints newline after text

# Function to slowly type out any general text with delay
def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Clears the screen when the program starts
clear()

# Start of the game loop
while True:
    slow_input("Do you want to play this game? ")
    game = input("> ")

    if game.lower() != "yes":
        slow_print("Damn, ok bye bro.")  # Ends game if player says no
        break

    # Ask for the player's name
    slow_input("> What is your name: ")
    name = input("> ")

    # Special responses for specific names
    if name.lower() in ["salah", "aran"]:
        slow_print("Bro you're so cool and awesome")
    elif name.lower() == "cole":
        slow_print("PLEASE GIVE US 100 - Salah and Aran")
    elif name.lower() == "laith":
        slow_print("Ay stop touching our code")

    # Start Madlibs game
    slow_print(f"\nHello {name}, let's play a game of Madlibs.")

    # Get three adjectives from the user
    slow_input("\n> Give me one Adjective: ")
    adjective_one = input("> ")

    slow_input("\n> Come on gimme a better one: ")
    adjective_two = input("> ")

    slow_input("\n> Last one pretty please: ")
    adjective_three = input("> ")

    # Confirm the adjectives and move forward
    slow_print(f"{adjective_one}, {adjective_two}, and {adjective_three} are great choices. Let's see how they fit in the story of your choice.")

    # Ask user to pick a story
    slow_input("\n> Choose a story, [1] [2] [3]")
    try:
        story = int(input("> "))  # Try converting input to integer
    except ValueError:
        slow_print("That's not a number! Try again.")
        continue

    clear()  # Clear screen before showing story

    # Story 1: Monster attack at school
    if story == 1:
        slow_print(f"\nAfter a long Friday, {name} and his friends were ready for the weekend. All was well until the {adjective_one} monster appeared! It chased {name} and friends around the school. Then all of a sudden the superhero {adjective_two} man appeared! They said not to worry as they beat the {adjective_one} monster to a pulp! As local authorities take the monster away, {name} and friends told the superhero that he really is {adjective_three}!")

    # Story 2: Chocolate shop adventure
    elif story == 2:
        slow_print(f"\n{name} was walking through his city and stumbled across a chocolate shop called The {adjective_one} Chocolatier. He went in with an open mind and chose the {adjective_two} chocolate. They also wrapped it up nicely and you get to choose the packaging. {name} chose a {adjective_three} wrapping! {name} left with a sweet treat and a big smile!")

    # Story 3: Fantasy adventure with fighting
    elif story == 3:
        # Get more inputs because this is a more interactive story
        slow_input("> Give me a number, pretty please: ")
        number_1 = input("> ")

        slow_input("> That was a pretty shit number, give me a mythical creature: ")
        mythical_creature = input("> ")

        slow_input("> Give me a special wizard-type ability: ")
        special_ability = input("> ")

        clear()
        slow_print("Ok then, here's your story!")
        slow_print(f"\n{name} was walking through the forest. It took about {number_1} days to reach the castle. His {adjective_one} blade was carrying him throughout the night. Later on, the {adjective_two} {mythical_creature} appeared in his peripheral vision. You whip out the blade to fight the {adjective_three} peasants that work for the {mythical_creature}.")

        # Using the slow_input function this is the decision making part of what you want to do in your story
        slow_input("\n> You have the option to run away and save yourself! Would you like to run? Yes or No: ")
        choice = input("> ")

        #if you chose yes, you are given the prompt to try again using the while loop function
        while choice.lower() == "yes":
            slow_print(f"You've got small balls. You chose to run, the {adjective_three} peasants caught you. They tortured you then put you into a guillotine. YOU DIED.")
            slow_input("> Try again... Would you like to run? Yes or No: ")
            choice = input("> ")

        if choice.lower() == "no":
            slow_print("Wow, you've got balls. Anyways, you chose to fight them off.")
            clear()
            slow_input("> You discovered a crossbow in your backpack along with your sword. Choose one of them as your weapon: ")
            weapon = input("> ")

            #if you chose yes, you are given the prompt to try again using the while loop function
            while weapon.lower() == "sword":
                slow_print("\nStupid choice, they all brought guns to a fist fight I guess. You died to the peasants.")
                slow_input("> Try again. Choose your weapon: sword or crossbow: ")
                weapon = input("> ")

            if weapon.lower() == "crossbow":
                slow_input(f"\n> Using your crossbow, you shot at the {mythical_creature}. It used its ability, {special_ability}, and blocked your projectile. Would you like to run? Yes or No: ")
                run_decision = input("> ")

                while run_decision.lower() == "no":
                    slow_print(f"\nYou got balls. But the {mythical_creature} pelted you with {special_ability}. YOU DIED!")
                    slow_input(f"\n> Try again... Would you like to run this time? Yes or No: ")
                    run_decision = input("> ")

                if run_decision.lower() == "yes":
                    slow_print("\nEven though you made a fearful decision, it was a good one. You ran into the forest behind you and realized there are more peasants.")
                    slow_input(f"\n> The {mythical_creature} and the {adjective_three} peasants are cornering you. Do you fight back? Yes or No: ")
                    death = input("> ")

                    if death.lower() == "no":
                        slow_print("\nYeah sorry, no getting out of this one. You're dead anyways. No fighting back. Sorry.")
                    elif death.lower() == "yes":
                        slow_print("\nI think you forgot you're cornered buddy. You're dead. Sorry. The End.")

    else:
        # If invalid story choice it shows this code
        slow_print("That story doesn't exist. Choose 1, 2, or 3 next time.")

    # These lines of code asks the user if they want to play again, if no the terminal is not able to be typed in.
    clear()
    slow_input("\n> Do you want to play this game again? Yes or No: ")
    play_again = input("> ")
    if play_again.lower() != "yes":
        slow_print("Thanks for playing, Bye!")
        break
