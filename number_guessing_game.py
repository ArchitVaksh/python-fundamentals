import random
secret_number = random.randint(1,100)
count = 1
while count<=6:
    try:
        guess = int(input("Guess a number (1-100): "))
        if guess == secret_number:
            print("Correct!")
            print("You have guessed the number in", count, "attempts")
            break
        elif guess > secret_number:
            print("Too High!")
        elif guess < secret_number:
            print("Too Low!")
        count += 1
        if count == 6 and guess != secret_number:
            print("Game over!")
            print(f"The correct number was: {secret_number}")
            break
    except:
        print("Invalid input, try again")
