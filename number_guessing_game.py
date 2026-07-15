import random
secret_number = random.randint(1,100)

while True:
    guess = int(input("Guess a number (1-100): "))
    if guess == secret_number:
        print("Correct!")
        break
    elif guess > secret_number:
        print("Too High!")
    elif guess < secret_number:
        print("Too Low!")
