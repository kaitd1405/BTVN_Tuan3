def xd10(a):
    if ('1' in a) :
        return True
    else :
        return False
def ss10(a,b):
    s = {a.replace('0','1'),b.replace('0','1')}
    if (len(s)==1) :
        return True
    else :
        return False
a = list(map(str,input().split()))
check = {}
ans=[]
for i in a :
    ok = True
    for j in ans :
        if (ss10(i,j)) :
            ok=False
    if ok==True :
        ans.append(i)

print(' '.join(ans))