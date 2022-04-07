from random import randint
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print(''' escolha um 
            [0] Pedra
            [1] Papel
            [2] Tesoura
''')
jogador = int(input('Qual é a sua jogada? '))

print(f'o computador escolheu {itens[computador]}')

if computador == 0:
    if jogador==0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador ganhou')
    elif jogador == 2:
        print('computador ganhou')
    else:
        'jogada invalida'
elif computador == 1:
    if jogador==0:
        print('jogador perdeu')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador ganhou')
    else:
        'jogada invalida'
elif computador == 2:
    if jogador==0:
        print('jogador ganhou')
    elif jogador == 1:
        print('Jogador perdeu')
    elif jogador == 2:
        print(' ')
    else:
        'jogada invalida'