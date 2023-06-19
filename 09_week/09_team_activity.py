print ('Enter a list of numbers, type 0  when finished.')

numbers = []
new_number = None
sum = 0
count = 0
average = 0

while new_number != 0:
    new_number = int(input('Enter number: '))
    
    if new_number != 0:
        numbers.append(new_number)
        count += 1

for number in numbers:
    sum += number

average = sum / len(numbers)
largest = (max(numbers))
print(f'The items are: {numbers}')
print(f'The sum is: {sum}')
print(f'The total of items are: {count}')
print(f'The average is: {average}')
print(f'The largest number is : {largest}')