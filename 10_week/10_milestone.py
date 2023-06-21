menu = ['Add item','View cart','Remove item','Compute total','Quantity of Items','Update Item','Quit']
cart = []
prices = []
count = 0
action = None

while action != '7':

    print('\nPlease select one of the following: ')

    for option in menu:
        count += 1
        print(f'{count}. {option}')
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

    if action == '5':
        total_items = len(cart)
        print(f"You have listed '{len(cart)}' item/s in your cart.")

    if action == '6':
        while True:
            update_item = int(input('Which item would you like to update? '))
            update_item = update_item - 1
            if update_item >= 0 and update_item < len(cart):
                    new_price = float(input('Enter the new price: '))
                    # Update the price of the selected item
                    prices[update_item] = new_price
                    print('Item price updated.')
                    print()
                    break
            else:
                print('That is not a valid index of the list')
                print()

print('Thank you. Goodbye.')