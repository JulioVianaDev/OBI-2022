def bt(k,base,restante):
    if(k == 0):
        if(restante == 0):
            return 1
        return 0
    if(base>restante):
        return 0
    ret = 0 
    for v in range(base,restante+1):
        ret += bt(k-1,v+1,restante-v)
    return ret
[R,K] = [int(c) for c in input().split()]
print(bt(K,1,R))