import random
def number_to_guess():
    global secret_number
    secret_number = random.randint(1,100)
    return secret_number
number_to_guess()
count = 1
while count<=6:
    try:
        guess = int(input("Guess a number (1-100): "))
        if guess == secret_number:
            print("Correct!")
            print("You have guessed the number in", count, "attempts")
            again = input("Do you want to play again? (y/n): ").upper()
            if again == "Y":
                count = 1
                number_to_guess()
                continue
            elif again == "N":
                print("Thank you for playing!")
                break
        elif guess > secret_number:
            print("Too High!")
        elif guess < secret_number:
            print("Too Low!")
        count += 1
        if count == 6 and guess != secret_number:
            print("Game over!")
            print(f"The correct number was: {secret_number}")
            again = input("Do you want to play again? (y/n): ").upper()
            if again == "Y":
                count = 1
                number_to_guess()
                continue
            elif again == "N":
                print("Thank you for playing!")
                break
    except:
        print("Invalid input, try again")
