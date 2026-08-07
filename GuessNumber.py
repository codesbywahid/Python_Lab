
import random
secret_number = random.randint(1, 100)
guess = 0
attempts = 0

while guess != secret_number:
    try:
        guess = int(input("Enter your guess number (1-100): "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if guess > secret_number:
            print("Too high! Choose a smaller number.")
        elif guess < secret_number:
            print("Too low! Choose a bigger number.")
        else:
            print("🎉 Congratulations! You guessed it.")
            print(f"You guessed the number in {attempts} attempts.")

    except ValueError:
        print("Invalid input! Please enter a whole number.")
        print("You guessed the number in {attempts} attempts.")