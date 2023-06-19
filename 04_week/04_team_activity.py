import math

print(f"Welcome to the velocity calculator. Pleas enter the following: ")
m = float(input(f"Mass (in kg): "))
g = float(input(f"Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input(f"Time (in seconds): "))
p = float(input(f"Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input(f"Cross sectional area (in m^2): "))
C = float(input(f"Drag constant (o.5 for sphere, 1.1 for cylinder): "))

#calculate the formula with the values
c = (1/2) * p * A * C
velocity = math.sqrt((m*g)/c) * (1 - math.exp(- (math.sqrt(m*g*c)/m)*t))
print()
print(f"The inner value of c is : {c:.3f}")
print(f"The velocity after {t:.3f} seconds is: {velocity:.3f} m/s")