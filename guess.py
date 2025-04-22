#program to guess the number

secret_number = 7  
guess = None

print("Guess the secret number between 1 and 10")

while guess != secret_number:
    guess = int(input("Enter your guess"))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("You got it")

print("game over")
