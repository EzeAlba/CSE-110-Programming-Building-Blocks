secret = 'home'
print('Welcome to the word guessing game!')
print()

guess = input('What is your guess? ').lower()
count = 1

while secret != guess : 
    count = count+1
    print ('Your guess was not correct.')
    guess = input('What is your guess? ').lower()

print('Congratulations! You guessed it!')
print(f'It took you {count} guesses.')