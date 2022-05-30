from random import randint
numero  = randint(0,15)
if numero %  2 ==0:
    print("par")
else:
    print("impar")
escolhido = int(input("escolha um numero"))
if escolhido == numero:
    print("adivinhou")
else:
    print("errou")