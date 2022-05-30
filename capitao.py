[moeda,marinheiros] = [int(c) for c in input().split()]
partes = moeda // (marinheiros + 2)
print(partes*2)