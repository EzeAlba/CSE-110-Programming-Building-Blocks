names_list = []
balances_list = []
name = None
balance = None

print('Enter the names and balances of bank accounts (type: quit when done)')
while name != 'quit':
    name = input('Please type the name of the bank account: ')
    if name != 'quit':
        balance = float(input('Please type the current balance: '))
        names_list.append(name)
        balances_list.append(balance)

total_balance = sum(balances_list)
average = total_balance/len(balances_list)


print('\nAccount Information:')
for i in range(len(names_list)):
    print(f'{i}.{names_list[i]} - ${balances_list[i]}')
print()
print(f'Total: ${total_balance}')
print(f'Average: ${average}')

max_balance = balances_list.index(max(balances_list))
print(f'The Highest balance: {names_list[max_balance]} - ${balances_list[max_balance]} ')

while True:
    update_choice = input("\nDo you want to update an account? (yes/no) ")
    if update_choice.lower() == "no":
        break
    elif update_choice.lower() != "yes":
        continue

    account_index = int(input("What account index do you want to update? "))
    if 0 <= account_index < len(balances_list):
        new_balance = float(input("What is the new amount? "))
        balances_list[account_index] = new_balance
    
    total_balance = sum(balances_list)
    average = total_balance/len(balances_list)
    print()

    print('Account Information:')
    
    for i in range(len(names_list)):
        print(f'{i}.{names_list[i]} - ${balances_list[i]}')
    print()
    print(f'Total: ${total_balance}')
    print(f'Average: ${average}')
    max_balance = balances_list.index(max(balances_list))
    print(f'The Highest balance: {names_list[max_balance]} - ${balances_list[max_balance]} ')



