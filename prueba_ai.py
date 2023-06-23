import math

life_expectancy_csv = []
entity = []
code = []
year = []
life_expectancy = []
interest_year_list = []
count = 0
sum = 0

interest_year = int(input('Enter the year of interest: '))
print()

with open(r'C:\Users\Spread\Documents\Eze Code\CSE 110 Programming Building Blocks\11_week\life-expectancy.csv') as csv_file:
    next(csv_file)
    for line in csv_file:
        csv_line = line.split(',')
        entity.append(csv_line[0])
        code.append(csv_line[1])
        year.append(csv_line[2])
        life_expectancy.append(float(csv_line[3].strip()))
        
        if interest_year == int(csv_line[2]):
            interest_year_list.append(csv_line)

overall_max_index = life_expectancy.index(max(life_expectancy))
overall_min_index = life_expectancy.index(min(life_expectancy))

print(f"The overall max life expectancy is: {max(life_expectancy):.3f} from {entity[overall_max_index]} in {year[overall_max_index]}")
print(f"The overall min life expectancy is: {min(life_expectancy):.3f} from {entity[overall_min_index]} in {year[overall_min_index]}")

print(f"\nFor the year {interest_year}:")
average = sum(life_expectancy) / len(interest_year_list)
print(f"The average life expectancy across all countries was {average:.2f}")

year_max_index = interest_year_list.index(max(interest_year_list, key=lambda x: float(x[3].strip())))
year_min_index = interest_year_list.index(min(interest_year_list, key=lambda x: float(x[3].strip())))

print(f"The max life expectancy was in {interest_year_list[year_max_index][0]} with {float(interest_year_list[year_max_index][3].strip()):.2f}")
print(f"The min life expectancy was in {interest_year_list[year_min_index][0]} with {float(interest_year_list[year_min_index][3].strip()):.2f}")
