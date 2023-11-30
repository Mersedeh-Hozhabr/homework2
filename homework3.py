a = int(input('enter a:'))
b = int(input('enter b:'))
c = int(input('enter c:'))
if a+b>c and a+c>b and c+b>a:
    print('It is possible to draw the triangle')
else:
    print('It is not possible to draw the triangle')