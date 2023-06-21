life_expectancy_csv = []
entity = []
code = []
year = []
life_expectancy = []

with open(r'C:\Users\Spread\Documents\Eze Code\CSE 110 Programming Building Blocks\11_week\life-expectancy.csv') as csv_file:
    next(csv_file)
    for line in csv_file:
        csv_line = line.split(',')
        entity.append(csv_line[0])
        code.append(csv_line[1])
        year.append(csv_line[2])
        life_expectancy.append(csv_line[3])
        #print(csv_line)
#print(life_expectancy)
print(f'The overall max life expectancy is: {max(life_expectancy)}')
print(f'The overall min life expectancy is: {min(life_expectancy)}')
