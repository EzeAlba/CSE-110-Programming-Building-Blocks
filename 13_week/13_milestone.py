import math

def wind_chill(T,V):
    chill_temp = 35.74 + (0.6215 * T) - (35.75*(V**0.16)) + ((0.4275*T)*(V**0.16))
    return chill_temp

def celsius_convert(degrees):
    return (degrees*(9/5)) + 32

count = 5
temperature = float(input('Plase enter a temperature: '))
degrees = input('Fahrenheit or Celsius (F/C)? :')
#speed = float(input('Please enter the speet: '))

if degrees.lower() == 'c':
    temperature = celsius_convert(temperature)
    print(f'Temperature in fahrenheit: {temperature}')
    
while count < 61:
    calculation = wind_chill(temperature,count)
    print(f'At temperature {temperature}F, and wind speed {count} mph, the windchill is: {calculation:.2f}F' )
    count += 5
