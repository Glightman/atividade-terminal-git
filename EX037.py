
""" Exercício Python 37:
 Escreva um programa em Python que leia
  um número inteiro qualquer e peça para o usuário 
  escolher qual será a base de conversão:
   1 para binário, 2 para octal e 3 para hexadecimal. """

num = int(input('Digite um numero qualquer: '))
print('''escolha uma das bases para conversão:
[ 1 ] coverter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('O número digitado não é válido.')