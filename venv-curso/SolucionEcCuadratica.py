import math

a=int(input('Dame a:'))
b=int(input('Dame b:'))
c=int(input('Dame c:'))

if a!=0: 
    d= b**2-4*a*c
    if d>=0:
        x1 = (-b + math.sqrt(b**2 -4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2 -4*a*c))/(2*a)
        print('x1=', x1, '\nx2',x2)
    else:
        print('solucion comleja')
else:
    print('no es una ecuacion cuadratica, es linea')

print('continua')
# sc Secuenciales
# sc condicionales (if, if-else, elif )
# SC Ciclicas (While, for)