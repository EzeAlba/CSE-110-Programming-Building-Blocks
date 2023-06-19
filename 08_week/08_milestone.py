import random

print('Welcome to the word guessing game!')
print()

words = ['hello','fantastic','coding','watermelon','argentina','pancakes']
secret = random.choice(words)
number_of_letters = len(secret)
hint = ['_'] * number_of_letters
count = 0

while True:
    hint_str = ' '.join(hint)
    print(f'Your hint is: {hint_str}')
    guess = str(input('What is your guess: ').lower())
    count = count+1

    if number_of_letters != len(guess):
        print('Sorry, the guess must have the same number of letters as the secret word.')
        continue

    if guess.lower() == secret.lower():
        print('Congratulations! You guessed it!')
        print(f'It took you {count} guesses.')
        break
    
    for i in range(number_of_letters):
        if guess[i] == secret[i]:
                hint[i] = secret[i].upper()
        elif guess[i] in secret:
            hint[i] = guess[i].lower()
        else:
            hint[i] = '_'
    print() 
