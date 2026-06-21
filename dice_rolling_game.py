# %%
import random


def game():
    roll_counter = 0
    while True:
        start_game = str(input("Roll the dice? (y/n): ")).lower()
        if start_game == "y" or start_game == "n":
            pass
        else:
            print("Invalid choice!")
        if start_game == "n":
            print("Thanks for playing")
            print(f"dice rolled: {roll_counter}")
            break
        elif start_game == "y":
            dices = int(input("how many dice?"))
            for i in range(dices):
                roll_counter += 1
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                print(f"({dice1}, {dice2})")
            i += i


game()
# %%
