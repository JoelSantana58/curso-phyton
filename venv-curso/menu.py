import math

i=1
while i<=5
    print('MENÚ')
    print('1.Area Triangulo')
    print('2.Salario de trabajador')
    print('3.solucion de ec. cuadratica')
    print('4.Edad')
    print('5.salir')
    n=n+1
opc = int(input('Dame una opcion'))

if opc == 1:
    a=int (input('dame el lado a:'))
    b=int (input('dame el lado b:'))
    c=int (input('dame el lado c:'))

    s=(a+b+c)/2

    area=math.sqrt(s(s-a)(s-b)(s-c))

    print('el area es:%.2f' %area)

elif opc == 2:
    nombre= input('nombre:')
    ht = int (input('horas trabaadas:'))
    ph = float (input('Pago por hora:'))

    salario = ph*ht

    print('el salario de:' .nombre, 'es $', salario )
elif opc == 3:
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
elif opc == 4:
    n= int(input('numero entre 0 y30'))
    if n>=0 and n<=20:
        print('rango 11 al 20')
    elif n>10 and n<=20:
        print('rango del 11 al 20')
    elif n>20 and n<=30:
        print ('rango del 21 al 30')
    else:
        print('fuera de rango')
elif opc == 5:
    print('REgrese pronto')
