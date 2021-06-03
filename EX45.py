""" Exercício Python 45: 
Crie um programa que faça 
o computador jogar Jokenpô com você """

from random import randint
itens = ('pedra', 'papel', 'tesoura') #coloquei os itens dentro de uma tupla
computador = randint(0, 2) #usei o randint para selecionar a posição da opção na tupla
#print('Computador jogou: {}'.format(itens[computador]))
print('''As suas opções são: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=-'*15)#apenas para customizar o código
print('Computador jogou: {}'.format(itens[computador]))
print('Jogador jogou: {}'.format(itens[jogador]))
print('-=-'*15)
comp = itens[computador]
jog = itens[jogador]
if comp == 'pedra' and jog == 'papel':
    print('VOCÊ GANHOU!')
elif comp == 'papel' and jog == 'tesoura':
    print('VOCÊ GANHOU!')
elif comp == 'tesoura' and jog == 'pedra':
    print('VOCÊ GANHOU!')
elif jog == 'pedra' and comp == 'papel':
    print('O COMPUTADOR GANHOU!')
elif jog == 'papel' and comp == 'tesoura':
    print('O COMPUTADOR GANHOU!')
elif jog == 'tesoura' and comp == 'pedra':
    print('O COMPUTADOR GANHOU!')
elif comp == jog:
    print('EMPATE!!!')