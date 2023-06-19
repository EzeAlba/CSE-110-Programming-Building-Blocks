can_ride = False

height = int(input('Please enter the height of the first rider: '))
age = int(input('Please enter the age of the first rider: '))
second_rider = input('Is there a second rider? (yes or no): ').lower()

if second_rider == 'yes':
    second_height = int(input('What is the height of the second rider? '))
    second_age = int(input('What is the age of the second rider? '))
    if height < 62 and second_height < 62 and age < 18 and second_age < 18:
        can_ride = False
        
        if age <= 12 and second_age <= 12 and height <= 52 and second_height <= 52:
            can_ride = True
    else:
        can_ride = True
    if (age >= 12 and age <= 17) or (second_age >= 12 and second_age <=17):
        gold_pass = input('Do you have a golden passport? (yes or no): ').lower()
        if gold_pass == 'yes':
            can_ride = True
        else: 
            if (age >= 16 and second_age >= 14) or (age >= 14 and second_age >= 16):
                can_ride = True
        
elif second_rider == 'no' and age < 18 and height < 62:
    can_ride = False
    
if can_ride:
    print('You are allowed to ride')
else:
    print('Sorry you are not allowed to ride')