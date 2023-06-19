menu = ['Add item','View cart','Remove item','Compute total','Quit']
cart = []
count = 0
action = None

while action != 5:
    print('Please select one of the following: ')

    for option in menu:
        count += 1
        print(f'{count}. {option}')
    count = 0

    action = int(input('Please enter an action: '))
    if action == 1:
        new_item = input('What item would you like to add? ')
        cart.append(new_item)
        print(f"'{new_item}' has been added to the cart.")
        print()

    if action == 2:
        print('The contents of the shopping cart are: ')
        for item in cart:
            print(item)
        print()

print('Thank you. Goodbye.')
