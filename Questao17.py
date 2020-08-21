area = float(input("area a ser pintada"))
litros = area/3
precoL = 80.0 
capacidadeL = 18
latas = litros / capacidadeL 
valor = latas * precoL
print ('Você usara {:.1f}latas de tinta'.format(latas))
print ('O preco total é de: R${:.2f}'.format(valor))
