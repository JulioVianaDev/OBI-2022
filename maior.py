a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))

menor = a 

if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando se ele é maior
maior = a 
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f' o maior numero é {maior} e o menor {menor}')

