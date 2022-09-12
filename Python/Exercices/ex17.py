# ex 17

from math import sqrt

a=1

for i in range(1,1000):
    a=a+1/i**2

print(sqrt(6*a))