
#This is a Mad Lib game code. 
#The purpose is to ask the user to introduce words and then show how this words
#are used to tell a story.

print('Please enter the following:')
print()

adjective = input('adjective: ')
animal = input('animal: ')
verb1 = input('verb: ')
exclamation = input('exclamation: ')
verb2 = input('verb: ')
verb3 = input('verb: ')
exclamation2 = input('exclamation: ')
name = input('name: ')
print()
print('Your story is:')
print()

print('The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective} {animal} {verb1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all') 
print(f'I could think to do was to {verb2} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb3}')
print(f'right in front of my family. Then my family said "{exclamation2.capitalize()}!"') 
print(f'And finally my little brother {name} started to cry. So everyone got mad at me.')