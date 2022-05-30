n=int(input())
m=int(input())
album=[]
for i in range(m):
    x = int(input())
    if x not in album:
        album.append(x)
# escreve a resposta
print(n-len(album))