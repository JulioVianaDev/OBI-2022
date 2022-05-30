N = int(input("Numero de participantes: "))
tamanhos = [int(i) for i in input().split()]
camisa_peq = int(input())
camisa_med = int(input())

pref_peq = tamanhos.count(1)
pref_med = tamanhos.count(2)

if camisa_peq < pref_peq or camisa_med < pref_med:
    print("N")
else:
    print("S")

