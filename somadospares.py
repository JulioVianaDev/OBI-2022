soma = 0
cont = 0

for c in range(1,7):
    num = int(input(f'digite {c} valor'))
    if num % 2 == 0:
        soma+=num
        cont +=1
print(f'Voce informou {cont} numeros pares e a soma foi {soma}')