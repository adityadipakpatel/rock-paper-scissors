import random

# predefined questions
distracting_questions = [
    "What's your favorite color?",
    "If you could have any superpower, what would it be?",
    "What's the last movie you watched?",
    "If you were an animal, which one would you be?",
    "What's your dream vacation destination?",
    "What's your favorite type of music?",
    "What's your go-to comfort food?",
    "What’s the last book you read?",
    "Who’s your favorite superhero?",
    "What’s your favorite childhood memory?",
]

# sequence is Rock -> Paper -> Scissors
moves = ["Rock", "Paper", "Scissors"]
computer_last_move = "Rock"  # Always start with "Rock" after the question
result_tracker = None  # Tracks if last round was Win, Lose, or Tie

def get_computer_move():
    global computer_last_move, result_tracker

    if result_tracker == "Win": # move forward
        computer_last_move = moves[(moves.index(computer_last_move) + 1) % 3]
    elif result_tracker == "Lose": # move backward
        computer_last_move = moves[(moves.index(computer_last_move) - 1) % 3]
    # if tie, repeat same move
    return computer_last_move

# determine winner using this function
def determine_winner(user_move, computer_move):
    if user_move == computer_move:
        return "Tie"
    elif (
        (user_move == "Rock" and computer_move == "Scissors") or
        (user_move == "Paper" and computer_move == "Rock") or
        (user_move == "Scissors" and computer_move == "Paper")
    ):
        return "User"
    else:
        return "Computer"

# main game loop
def play_game():
    global result_tracker

    print("Welcome to Rock-Paper-Scissors!")
    print("Let's play! I have a strategy, but can you beat me?")

    # ask random distracting question which makes user to more likely choose "scissors"
    question = random.choice(distracting_questions)
    print(f"\n{question}: ", end="")
    tmp = input("")
    print("Thanks for the answer\n\nNow, lets play")

    while True:

        # user input
        user_move = input("Choose Rock, Paper, or Scissors (or type 'exit' to quit): ").capitalize()
        if user_move == "Exit":
            print("Thanks for playing! Goodbye!")
            break

        if user_move not in moves:
            print("\nInvalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        # bot's move based on strategy
        computer_move = get_computer_move()

        # print chosen moves
        print(f"\nYou chose: {user_move}")
        print(f"Computer chose: {computer_move}")

        # determine winner
        winner = determine_winner(user_move, computer_move)

        if winner == "Tie":
            print("Tie!")
            result_tracker = "Tie"
        elif winner == "User":
            print("You win!")
            result_tracker = "Lose"
        else:
            print("Bot wins!")
            result_tracker = "Win"

if __name__ == "__main__":
    play_game()

