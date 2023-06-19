#asking values to user
print('Please enter the following information:')
print()
first_name = input('First name: ')
last_name = input('Last name: ')
email = input('Email adress: ')
phone = input('Phone number: ')
job = input('Job title: ')
id = input('ID Number: ')
hair_color = input('Hair color: ')
eyes_color = input('Eye color: ')
month = input ('Starting month: ')

#Asking a yes/no question 
training = input('Completed advanced training? Yes/No: ')
while training.lower() != 'yes' and training.lower() != 'no':
    print('\nPlease respond Yes or No to continue.')
    training = input('Completed advanced training? Yes/No: ')
print('')

#Showing the final result
print('The ID Card is:')
print('----------------------------------------')
print(last_name.upper() + ', ' + first_name.capitalize())
print(job.title())
print('ID: ' + id)
print('')
print(email.lower())
print(phone)
print('')
print('Hair: {:<15} Eyes: {:<15}'.format(hair_color.capitalize(), eyes_color.capitalize()))
print('Month: {:<14} Training: {:<15}'.format(month.capitalize(), training.capitalize()))
print('----------------------------------------')

