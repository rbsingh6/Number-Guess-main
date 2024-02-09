import random

r = random.randint(0, 100)
count = 1

while (1):
    num = int(input("Enter a number for guess: "))
    if (num > r):
        print("Your guess is high! Please enter a lower number.")
    elif (num < r):
        print("Your guess is low! Please enter a higher number.")
    elif (num == r):
        print("\nCongratulations! You guessed the number.\n")
        print(f"You guessed the number in {count} tries.\n")
        break
    count = count + 1