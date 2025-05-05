from akinator.async_aki import Akinator
import asyncio

aki = Akinator()

async def main():
    print("Welcome to Akinator!")
    await aki.start_game(language="en")

    while aki.progression <= 80:
        print(aki.question)
        answer = input("Your answer (yes/no/idk/probably/probably not): ").lower()

        try:
            if answer not in ['yes', 'no', 'idk', 'probably', 'probably not']:
                print("Invalid answer. Please try again.")
                continue

            await aki.answer(answer)
        except Exception as e:
            print(f"Error: {e}")
            break

    await aki.win()
    print(f"\nI guess: {aki.first_guess['name']} ({aki.first_guess['description']})")
    print(f"Image: {aki.first_guess['absolute_picture_path']}")
    correct = input("Was I correct? (yes/no): ").lower()
    if correct == "yes":
        print("Yay! I guessed it right 😎")
    else:
        print("Oh no! Maybe next time 😢")

asyncio.run(main())