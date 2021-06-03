from random import randint
from time import sleep
cont = 1
print('-=-'*20)
print('A maquina está pensando em um número de 0 a 10...    ','AGUARDE...')
print('Você tem apenas 4 chances!')
print('-=-'*20)
sleep(5)
computador = randint(0,10)
print('Pronto!...')
sleep(1)
jogador = int(input('TENTE DESCOBRIR EM QUE NÚMERO EU PENSEI...: '))
while jogador != computador and cont<4:
    print('....')
    sleep(1)
    jogador = int(input('HUMMM... Não foi dessa vez, Tente de novo: '))
    cont += 1
if jogador == computador:
    print('-=-'*20)
    print('PARABÉNS!!! VOCÊ ACERTOU!')
    print('A máquina pensou no número {}'.format(computador))
    print('-=-'*20)
    print('Foram necessárias {} tentativas para acertar'.format(cont))
    print('-=-'*20)
else:
    print('....')
    sleep(1.5)
    print('Ahh! Não...')
    sleep(1)
    print('Suas chances acabaram! :(')

