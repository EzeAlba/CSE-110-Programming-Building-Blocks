#from colorama import Fore #import library that allows me to change the text colors
from colorama import Fore 

# Define a list of valid color choices
valid_colors = ['BLACK', 'BLUE', 'CYAN', 'GREEN', 'LIGHTBLACK_EX', 'LIGHTBLUE_EX', 'LIGHTCYAN_EX', 'LIGHTGREEN_EX', 'LIGHTMAGENTA_EX', 'LIGHTRED_EX', 'LIGHTWHITE_EX', 'LIGHTYELLOW_EX', 'MAGENTA', 'RED', 'WHITE', 'YELLOW']

while True:
    # Ask the user to type their favorite color
    favorite_color = input('Please type your favorite color: ').upper()

    if favorite_color in valid_colors:
        # If the color is valid, set the color variable using Fore.__getattribute__()
        color = Fore.__getattribute__(favorite_color)

        # Prin the user favorite color
        print(color + 'This text will show up in your favorite color, which is: ' + favorite_color)
        break
    else:
        # If the color is not valid, suggest a valid color and tell the user to try again
        print('Sorry, that color is not valid. Please choose from the following options: ')
        print(valid_colors)