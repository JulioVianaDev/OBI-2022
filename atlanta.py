A = int(input())
B = int(input())
achou = False
for x in range(1,B+1):
    if B % x !=0:
        continue
    larg = B//x +2
    comp = x + 2
    if A == 2*(comp +larg)-4:
        achou = True
        break
if achou:
    print(larg,comp)
else:
    print(-1,-1)