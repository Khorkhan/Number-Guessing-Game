import random

def play_game():
    print("==========")
    print("Welcome to Guess the number game!")
    print("Guess the number between 1 - 100")
    print("==========")

    #random number 1 - 100
    secret_number = random.randint(1,100)
    attempts = 0
    max_attempts = 7

    while True:
        try:
            remaining_attempts = max_attempts - attempts
            print(f"\n Your guess left {remaining_attempts}")

            #input from player
            guess = int(input("Guess the number 1 - 100: "))
            attempts += 1

            #check condition
            if guess < 1 or guess > 100:
                print("Please enter 1 - 100")
            elif guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too much!")
            else:
                print(f"\n Correct! the Secret number is {secret_number}")
                print(f"Your Attempts {attempts}")
                break

            if attempts >= max_attempts:
                print("\n Game Over")
                print(f"Sorry the correct number is: {secret_number}")

        except ValueError:
            print("Please enter numbers only!")

play_game()