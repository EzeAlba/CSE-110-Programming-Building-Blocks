import random
magic = random.randint(1,100)
guess = int(input("What is your guess? "))
count = 1 
while magic != guess:
    count = count + 1
    if magic > guess :
        print("Higher")
    elif magic < guess:
        print("Lower")
    guess = int(input("What is your guess? "))

print("You guessed it!")
print(f'You used {count} guesses')