""" Exercício Python 36 (curso de python na plataforma curso em vídeo): 
Escreva um programa para aprovar o empréstimo bancário 
para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador 
e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário 
ou então o empréstimo será negado.
 """
casa = float(input('Valor da casa: '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
parcela = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar a casa de R${:.2f} em {} anos'.format(casa,anos),end='')
print('a prestação será de R${:.2f}'.format(parcela))
if parcela <= minimo:
    print('Empréstimo consedido.')
else:
    print('Empréstimo negado!')
