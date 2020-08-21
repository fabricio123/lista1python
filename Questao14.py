peso = float(input('qual foi o peso dos peixes'))
if peso > 50:
   excesso = peso - 50
   multa = excesso * 4.00
   print(' a multa a pagar por excesso de peso é R${}'.format(multa))
   print(' o seu excesso é: {} quilos' .format(excesso))
