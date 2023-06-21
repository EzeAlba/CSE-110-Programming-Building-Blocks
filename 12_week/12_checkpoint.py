people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
young_name =''
young_age = 100

for line in people:
    line_clean = line.split(' ')
    age = int(line_clean[1])
    
    if age < young_age:
        young_age = age
        young_name = line_clean[0]
    print(line_clean)
print(f'{young_name} is {young_age}')