[A1,D1,A2,D2] = [int(c) for c in input().split()]



A1= int(input())
D1= int(input())
A2= int(input())
D2= int(input())

resultado = -1
if(D1 == A2 and A1 > D2):
    resultado = 1
if(D2 == A1 and A2 > D1):
    resultado = 2

print(resultado) 