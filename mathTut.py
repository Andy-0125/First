x = 3.14
y = 5
z = 2
result = max(x, y, z)
result2 = min(x, y, z)

import math
print(math.pi)
print(math.e)
result3 = math.sqrt(x)

# print(result)
# print(result2)
# print(result3) 

result4 = math.ceil(y)   #round up
result5 = math.floor(y)  #round down

radius =float(input("Enter the radius of the circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is:{round(area,2)}cm^2")

a=float(input("Enter side A: "))
b=float(input("Enter side B:"))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"side C is: {round(c,2)}")