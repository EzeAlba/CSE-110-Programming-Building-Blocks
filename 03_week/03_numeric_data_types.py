#Practice converting user input to numeric data types and perform calculations

age = int(input('How old are you? '))
next_age = age + 1
print(f'On your next birthday, you will be {next_age}')
print()

eggs = int(input('How many egg cartons do you have? '))
eggs_total = eggs * 12
print(f'You have {eggs_total} eggs')
print()

cookies = float(input('How many cookies do you have? '))
people = float(input('How many people are there? '))
cookies2 = cookies / people
print(f'Each person may have {cookies2} cookies')