slh = float(input('qual é o seu salário por hora:'))
ht = int(input('quantas horas vc trabalha no dia'))
sbruto = slh * ht
descontoimp = (sbruto*11)/100
descinss = (sbruto*8)/100
sindicato = (sbruto*5)/100
sliquido = sbruto - (descontoimp + descinss + sindicato)


print('seu salario bruto é:R$', sbruto)
print(' o desconto do sindicato é:', sindicato)
print('o desconto do imposto de renda é:R$', descontoimp)
print('o desconto do INSS é  de R$', descinss) 
print('seu salario liquido é:R$', sliquido)


