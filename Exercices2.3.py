# -*- coding: cp1252 -*-
# Fabien Toune
# Exercices2.3
# Nov 1, 2012

import math

def multadd(a,b,c):
    return a*b+c

print multadd(.5,math.cos(math.pi/4),math.sin(math.pi/4))
print multadd(2, math.log(12,7), math.ceil(276/19.))

def yikes(x):
    base = math.e**-x
    a = x
    c = multadd(-1, base, 1)**0.5
    return multadd(a,base,c)

print yikes(5)
