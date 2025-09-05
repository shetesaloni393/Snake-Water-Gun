import random
choices = ['snake', 'water', 'gun']

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'snake' and computer == 'water') or \
         (user == 'water' and computer == 'gun') or \
         (user == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"

print("Welcome to Snake, Water, Gun Game!")
user_choice = input("Enter your choice (snake/water/gun): ").lower()

if user_choice not in choices:
    print("Invalid choice! Please choose from snake, water, or gun.")
else:
    computer_choice = random.choice(choices)
    print(f"Computer choose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
