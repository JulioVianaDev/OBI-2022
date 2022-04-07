from random import randint
computador = randint(0,10)

print('pensei em um numero de 0 a 10')
print('adivinhe ele')

acertou = False
palpites = 0 

while not acertou:
    jogador = int(input("qual é o seu palpite? "))
    palpites +=1
    if jogador == computador:
        acertou = True
        break;
    else:
        if jogador < computador:
            print('Mais... Tente novamente')
        else:
            print('Menos... Tente Novamente')
        
print(f'acertou com {palpites} tentativas')