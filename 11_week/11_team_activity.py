hr_system_file = []

with open(r"C:\Users\Spread\Documents\Eze Code\CSE 110 Programming Building Blocks\11_week\hr_system.txt") as hr_system_file:
    for line in hr_system_file:
        hr_system_file = line.split(' ')
        print(f'Name: {hr_system_file[0]}, Title: {hr_system_file[2]} ')