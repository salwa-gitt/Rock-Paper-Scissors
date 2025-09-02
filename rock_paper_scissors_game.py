import random

ROCK = "r"
SCISSORS = "s"
PAPER = "p"


emojis = {ROCK: "🪨", PAPER: "📃", SCISSORS: "✂️"}

choices = tuple(emojis.keys())

tie = 0
user_score = 0
computer_score = 0

def get_user_choice():

    while True:
        user_choice = str(input("Rock, Paper, or scissors? (r/p/s): ")).strip().lower()

        if user_choice  in choices:
            return user_choice
        else:
            print("Invalid choice!")
    
def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    global tie, user_score, computer_score

    if computer_choice == user_choice:
        print("It's tie...")
        tie += 1

    elif( 
        (user_choice == ROCK and computer_choice == 's') or \
        (user_choice == SCISSORS and computer_choice == 'p') or \
        (user_choice == PAPER and computer_choice == ROCK)):

        print(f"You Win!")
        user_score += 1
            
    else:
        print(f"You loose!")
        computer_score += 1

def over_all_winner():
    global tie, user_score, computer_score


    if user_score > computer_score:
        print(f"YOU WIN: {user_score}-{computer_score}")
    elif user_score < computer_score:
        print(f"YOU LOSE: {user_score}-{computer_score}")
    else:
        print(f"IT'S TIE! {user_score}-{computer_score}")


def play_game():
    global tie, user_score, computer_score
    tie = 0
    user_score = 0
    computer_score = 0

    while True:

        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)


        if user_score == 2 or computer_score == 2:
            break

    if not ask_to_play_again():
        return

    

def ask_to_play_again():
    

    while True:

        play_again = str(input("Want to continue? (y/n): ")).strip().lower()

        if play_again == 'y':
            print("Restarting the game...")
            play_game()
            return True
            
        elif play_again == 'n':
            print("Thanks for playing...")
            print(f"Tie: {tie}")
            print(f"Win: {user_score}")
            print(f"Loss: {computer_score}")
            print(f"Total: {user_score + computer_score + tie}")
            over_all_winner()
            return False
            
        else:
            print("Invalid text...")

play_game()