import math

a=int (input('dame el lado a:'))
b=int (input('dame el lado b:'))
c=int (input('dame el lado c:'))

s=(a+b+c)/2

area=math.sqrt(s(s-a)(s-b)(s-c))

print('el area es:%.2f' %area)

#OA: +,-,*,/,//,**,%
#OR: <,>=,==,!=
#OL: and,or,not