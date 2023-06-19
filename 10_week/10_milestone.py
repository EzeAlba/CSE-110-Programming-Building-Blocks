menu = ['Add item','View cart','Remove item','Compute total','Quit']
cart = []
prices = []
count = 0
action = None

while action != '5':

    print('\nPlease select one of the following: ')

    for option in menu:
        count += 1
        print(f'{count}. {option}')
    print(f"You have listed '{len(cart)}' item/s in your cart.")
    count = 0

    action = input('Please enter an action: ')
    print()
    if action == '1':
        new_item = input('What item would you like to add? ')
        cart.append(new_item)
        price = float(input(f"What is the price of '{new_item}': "))
        prices.append(price)
        print(f"'{new_item}' has been added to the cart.")
        print()

    if action == '2':
        print('The contents of the shopping cart are: ')
        for i in range(len(cart)):
            count += 1
            print(f'{count}. {cart[i]} - ${prices[i]:.2f}')
        count = 0
        print()
    
    if action == '3':
        while True:
            remove = int(input('Which item would you like to remove? '))
            remove = remove - 1
            if remove >= 0 and remove < len(cart):
                del cart[remove]
                del prices[remove]
                print('Item removed.')
                print()
                break

            else:
                print('That is not a valid index of the list')
                print()

                
    if action == '4':
        total_price = sum(prices)
        print(f'The total price of the items in the shopping cart is ${total_price:.2f}')
        print()

    #if action != 1 and action != 2 and action != 3 and action != 4 and action != 5 and 
print('Thank you. Goodbye.')