sexo = int(input('qual e o seu sexo? digite 1 para masculino e 2 para femimino'))
if sexo == 1:
    h1 = float(input('qual e a sua altura:'))
    pesoideal = (72.7*h1) - 58
    print('seu peso ideal é:', pesoideal)
if sexo == 2:
    h2 = float(input('qual e a sua altura:'))
    pesoideal2 = (62.1*h2) - 44.7
    print('seu peso ideal é:', pesoideal2)
