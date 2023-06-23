import math
life_expectancy_csv = []
#entity = []
#code = []
#year = []
life_expectancy = []
interest_year_list = []
min_number = -1
max_number = 9999999

expectancy_max = ''
country_max = ''
year_max = ''
expectancy_min = ''
country_min = ''
year_min = ''
sum = 0

interest_year = int(input('Enter the year of interest: '))
print()
with open(r'C:\Users\Spread\Documents\Eze Code\CSE 110 Programming Building Blocks\11_week\life-expectancy.csv') as csv_file:
    next(csv_file)
    for line in csv_file:
        csv_line = line.split(',')
        #entity.append(csv_line[0])
        #code.append(csv_line[1])
        #year.append(csv_line[2])
        life_expectancy.append(csv_line[3].strip())
            
        #finding the max number in life expectancy with its country and year
        if min_number < float(csv_line[3].strip()):
            expectancy_max = float(csv_line[3].strip())
            min_number = expectancy_max
            country_max = csv_line[0]
            year_max = csv_line[2]
            
        #finding the min number in life expectancy with its country and year
        if max_number > float(csv_line[3].strip()):
            expectancy_min = float(csv_line[3].strip())
            max_number = expectancy_min
            country_min = csv_line[0]
            year_min = csv_line[2]
        
        #In the next if statemant I append in a new list 
        #all the lines that contain the year typed by the user.
        if interest_year == int(csv_line[2]):
            interest_year_list.append(csv_line)
            
#Putting variables to their original values
min_number = -1
max_number = 9999999

#New list with the values of selected year
for life_exp in interest_year_list:
    #Summing all life expectancies 
    number = float(life_exp[3].strip())
    sum = sum + number
    
    #Getting the max life expectancy
    if min_number < float(life_exp[3].strip()):
        expectancy_2 = float(life_exp[3].strip())
        min_number = expectancy_2
        country_2 = life_exp[0]
        
    #Getting the min life expectancy
    if max_number > float(life_exp[3].strip()):
        expectancy_3 = float(life_exp[3].strip())
        max_number = expectancy_3
        country_3 = life_exp[0]
        
    
#Calculating the average of life expectancies
#from the selected year.
average = sum/len(interest_year_list)

#print(life_expectancy)
#print(f'The overall max life expectancy is: {max(life_expectancy)}')
print(f'The overall max life expectancy is: {expectancy_max} from {country_max} in {year_max}')
#print(f'The overall min life expectancy is: {min(life_expectancy)}')
print(f'The overall min life expectancy is: {expectancy_min} from {country_min} in {year_min}')

print(f'\nFor the year: {interest_year}')
print(f'The average life expectancy across all countries was {round(average,2)}')
print(f'the max life expectancy was in {country_2} with {expectancy_2}')
print(f'the max life expectancy was in {country_3} with {expectancy_3}')

