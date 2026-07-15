import random
secret_number = random.randint(1,100)
count = 0
while True:
    count += 1
    guess = int(input("Guess a number (1-100): "))
    if guess == secret_number:
        print("Correct!")
        print("You have guessed the number in", count, "attempts")
        break
    elif guess > secret_number:
        print("Too High!")
    elif guess < secret_number:
        print("Too Low!")
