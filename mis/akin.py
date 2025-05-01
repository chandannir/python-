import asyncio
from akinator_async import Akinator # type: ignore

async def main():
    aki = Akinator()
    try:
        question = await aki.start_game(language='en', child_mode=False, region='en')
        while aki.progression <= 80:
            print(question)
            answer = input("Answer (yes/no/idk/probably/probably not): ").lower()

            if answer == "yes":
                question = await aki.answer("y")
            elif answer == "no":
                question = await aki.answer("n")
            elif answer in ["idk", "don't know"]:
                question = await aki.answer("idk")
            elif answer == "probably":
                question = await aki.answer("p")
            elif answer == "probably not":
                question = await aki.answer("pn")
            else:
                print("Invalid answer.")

        await aki.win()
        print(f"Is it {aki.first_guess['name']} ({aki.first_guess['description']})?")
        final = input("yes/no: ").lower()
        if final == "yes":
            print("I guessed it!")
        else:
            print("I failed to guess it.")
    except Exception as e:
        print(f"An error occurred: {e}")

asyncio.run(main())