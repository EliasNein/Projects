# %%
import random


def main():

    def gameDifficulty():
        difficulty = int(input("easy [1], medium [2], hard [3]"))
        while difficulty > 3:
            difficulty = int(input("Choose number between 1 and 3"))
        if difficulty == 1:
            number = random.randint(1, 50)
            print("Choose number between 1 and 50")
        elif difficulty == 2:
            number = random.randint(1, 75)
            print("Choose number between 1 and 75")
        elif difficulty == 3:
            number = random.randint(1, 100)
            print("Choose number between 1 and 100")

        return number

    def game():
        number = gameDifficulty()
        attempts = 0
        max_attempts = 10

        while attempts < max_attempts:
            guess = int(input())
            if number != guess:
                if number < guess:
                    print(f"It's less than {guess}")
                else:
                    print(f"It's higher than {guess}")
            else:
                print(f"You guessed right: {number} -> {guess}")
                break

            attempts += 1

        if attempts == 10:
            print("You brutally failed")

    game()


if __name__ == "__main__":
    main()
# %%
