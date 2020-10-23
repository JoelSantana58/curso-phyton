
edad = 18

condicion =edad >= 18
print('condicion')

if condicion:
    print('ya puedes votar, Mayor de edad')
    pass
else:
    print('no puede votar')

print('algo')

# and, or not

n= int(input('numero entre 0 y30'))
if n>=0 and n<=20:
    print('rango 11 al 20')
elif n>10 and n<=20:
    print('rango del 11 al 20')
elif n>20 and n<=30:
    print ('rango del 21 al 30')
else:
    print('fuera de rango')
