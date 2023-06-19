grade = float(input("Please input the grade percentage: "))
letter = ''
print()

if grade >= 90.0 and grade < 100.001:
    letter = 'A'

elif grade >= 80.0 and grade < 90.0:
    letter = 'B'

elif grade >= 70.0 and grade < 80.0 :
    letter = 'C'

elif grade >= 60.0 and grade < 70.0 :
    letter = 'D'
    
elif grade < 60.0 :
    letter = 'F'


else:
    print(f'{grade} Is not a valid percentage')
    print()

print(f'Your grade is {letter}')
print()

if grade >= 70.0 and grade < 100.1:
    print('Congratulations! You passed the course!')
else:
    print('You did not passed the course!')
    
