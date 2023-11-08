import random

options = ['Scissors', 'Rock', 'Paper']
score = 0
rounds = 0

print("Welcome to the game")

while True:
    rounds += 1
    print("\n1. Scissors")
    print("2. Rock")
    print("3. Paper")
    userOption = options[int(input("Choose your option (1, 2 o 3): ")) - 1]
    computerOption = options[random.randint(0, len(options)-1)]

    print (f"{userOption} vs {computerOption} -", end=" ")

    if userOption == "Scissors" and computerOption == "Paper":
        score += 1
        print("You win")
    elif userOption == "Rock" and computerOption == "Scissors":
        score += 1
        print("You win")
    elif userOption == "Paper" and computerOption == "Rock":
        score += 1
        print("You win")
    elif userOption == computerOption:
        print("Draw")
    else:
        print("You lost")
    
    keep = input("\nDo you want to continue? (Yes or No) ")
    
    if keep == "No":
        break

print(f"Rounds: {rounds}")
print(f"Wins: {score}")