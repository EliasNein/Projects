# %%
import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

icons = {ROCK: "🪨", PAPER: "🧻", SCISSORS: "✂️"}
choices = tuple(icons.keys())


def player_move():
    while True:
        player_choice = str(input("(r/p/s)")).lower()
        if player_choice in choices:
            return player_choice
        else:
            print("Value Error!")
            continue


def computer_move():
    computer_choice = random.choice(choices)
    return computer_choice


while True:

    def play_game():
        player = player_move()
        computer = computer_move()
        if computer == player:
            print(f"Tie \nYou {icons[player]} | {icons[computer]} Computer".rstrip())
        elif (
            (computer == ROCK and player == PAPER)
            or (computer == PAPER and player == SCISSORS)
            or (computer == SCISSORS and player == ROCK)
        ):
            print(
                f"You win \nYou {icons[player]} | {icons[computer]} Computer".rstrip()
            )
        else:
            print(
                f"You loose \nYou {icons[player]} | {icons[computer]} Computer".rstrip()
            )

    play_game()

    play_again = str(input("Do you want to play again? (y/n)")).lower()
    if play_again != "y" and play_again != "n":
        print("Value Error")
    elif play_again == "n":
        print("Thanks for playing!")
        break
    else:
        continue
# %%
