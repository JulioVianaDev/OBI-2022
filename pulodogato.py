N= int(input())
p=[int(c) for c in input().split()]

pulos = 0
lajotas = 0
while(lajotas < N-1):
    #tentar pular duas lajotas
    if(lajotas+2 < N and p[lajotas+2] ==1):
        pulos+=1
        lajotas+=2
    else:
        #tenta pular uma lajota
        if(lajotas+1< N and p[lajotas+1] ==1):
            pulos+=1
            lajotas+=1
        else:
            #não da pra pular
            break
if(lajotas  == N-1):print(pulos)
else:print(-1)