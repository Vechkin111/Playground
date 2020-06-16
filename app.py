import math
# a*x^2 + b*x + c = 0

a = 1
b = 0
c = 16
d = b*b - 4*a*c
if d < 0: 
    print ("no roots here") 
elif d == 0:
    x = (-b)/(2*a)
    print ("single root")
    print ("x: ", x)
else:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print ("two roots")
    print ("x1: ", x1)
    print ("x2: ", x2)