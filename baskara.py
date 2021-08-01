# 2equação do segundo grau
import math
a = input('digite coeficiente a :')
a = float(a)
b = input('digite coeficiente b :')
b = float(b)
c = input('digite o coeficiente c:')
c = float(c)

delta = b*b - 4 * a*c

if delta < 0 or a == 0:
    print(' Não se trata de uma equação do segundo grau e não calcule; ')
else:
    x1 = (-b + math.sqrt(delta)) / 2*a
    x2 = (-b - math.sqrt(delta)) / 2*a
    print(f'{x1} and {x2}')
