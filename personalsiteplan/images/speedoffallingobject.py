import math
print()
print('Welcome to the velocity calculator. Please enter the following: ')
print()
m = input('Mass (in kg): ')
g = input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): ')
t = input('Time (in seconds): ')
p = input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): ')
A = input('Cross sectional area (in m^2): ')
C = input('Drag constant (0.5 for sphere, 1.1 for cylinder): ')
c = round((1 / 2) * float(p) * float(A) * float(C),3) 
v = round((math.sqrt(float(m) * float(g) / float(c))) * (1 - math.exp(-1 * (math.sqrt(float(m) * float(g) * float(c)) / float(m)) * float(t) )),3)
print()
print('The inner value of c is: ' + str(c))
print('The velocity after ' + str(t) + ' seconds is: ' + str(v))