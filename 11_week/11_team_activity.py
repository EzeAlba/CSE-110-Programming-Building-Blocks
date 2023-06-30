hr_system_file = []

with open(r"C:\Users\Spread\Documents\Eze Code\CSE 110 Programming Building Blocks\11_week\hr_system.txt") as hr_system_file:
    for line in hr_system_file:
        hr_system_file = line.split(' ')
        salary = (float(hr_system_file[3])/12)/2
        if hr_system_file[2] == 'Engineer':
            salary = salary + 1000.00
        print(f'{hr_system_file[0]} (ID: {hr_system_file[1]}), {hr_system_file[2]} - ${salary:.2f}')