from math import *
a = float(input('Введите параметр a: '))
z1=1-1/4*sin(2*a)**2+cos(2*a)
print("{0:.2f} {1:.2f}".format(a,  z1))
tmp=cos(a)**2+cos(a)**4
y=pow(2,tmp)
print("{0:.2f}".format(z1))
