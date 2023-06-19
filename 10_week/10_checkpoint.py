shopping_list = []
count = 0
item = None
change_index = None
change_item = None

print('Please enter the items of the shopping list (type: quit to finish):')
while item != 'quit':
    item = input('Item: ')

    if item != 'quit':
        shopping_list.append(item)
        count += 1 

print('The shopping list is:')

for i in shopping_list:
    print(i)
print()

print('The shopping list with indexes is:')
for i in range(len(shopping_list)):
    print(f'{i}. {shopping_list[i]}')
print()

change_index = int(input('Which item would you like to change?: '))
change_item = input('What is the new item?: ')
print()
shopping_list[change_index] = change_item

print('The shopping list with indexes is:')
for i in range(len(shopping_list)):
    print(f'{i}. {shopping_list[i]}')
print()