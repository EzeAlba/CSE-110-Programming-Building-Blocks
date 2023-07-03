import math

life_expectancy_csv = []
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

try:
    interest_year = int(input('Enter the year of interest: '))
except ValueError:
    print("Invalid input. Please enter a valid year.")
    exit()

print()
try:
    with open(r'C:\Users\Spread\Documents\Eze Code\CSE 110 Programming Building Blocks\11_week\life-expectancy.csv') as csv_file:
        next(csv_file)
        for line in csv_file:
            csv_line = line.split(',')
            life_expectancy.append(csv_line[3].strip())

            if min_number < float(csv_line[3].strip()):
                expectancy_max = float(csv_line[3].strip())
                min_number = expectancy_max
                country_max = csv_line[0]
                year_max = csv_line[2]

            if max_number > float(csv_line[3].strip()):
                expectancy_min = float(csv_line[3].strip())
                max_number = expectancy_min
                country_min = csv_line[0]
                year_min = csv_line[2]

            if interest_year == int(csv_line[2]):
                interest_year_list.append(csv_line)

    min_number = -1
    max_number = 9999999

    for life_exp in interest_year_list:
        number = float(life_exp[3].strip())
        sum = sum + number

        if min_number < float(life_exp[3].strip()):
            expectancy_2 = float(life_exp[3].strip())
            min_number = expectancy_2
            country_2 = life_exp[0]

        if max_number > float(life_exp[3].strip()):
            expectancy_3 = float(life_exp[3].strip())
            max_number = expectancy_3
            country_3 = life_exp[0]

    average = sum / len(interest_year_list)

    print(f'The overall max life expectancy is: {expectancy_max} from {country_max} in {year_max}')
    print(f'The overall min life expectancy is: {expectancy_min} from {country_min} in {year_min}')

    print(f'\nFor the year: {interest_year}')
    print(f'The average life expectancy across all countries was {round(average, 2)}')
    print(f'the max life expectancy was in {country_2} with {expectancy_2}')
    print(f'the max life expectancy was in {country_3} with {expectancy_3}')

except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {str(e)}")