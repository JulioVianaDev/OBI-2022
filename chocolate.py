N = int(input)
preco = []
soma = 0

for i in range(N):
    preco.append(int(input()))

preco.sort(reverse=True)

for i in range(0,len(preco)):
    if i% 3 == 2:
        continue
    soma += preco[i]

print(soma) 