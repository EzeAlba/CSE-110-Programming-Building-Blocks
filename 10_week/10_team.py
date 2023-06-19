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
print()

print('Account Information:')
for i in range(len(names_list)):
    print(f'{names_list[i]} - ${balances_list[i]}')
print()
print(f'Total: ${total_balance}')
print(f'Average: ${average}')



