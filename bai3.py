a = set(map(str,input().split()))
b = set(map(str,input().split()))
if (len(a)>len(b)) :
    a,b=b,a
if (len(b-a)==len(b)-len(a)) :
    print("la tap con")
else :
    print("Khong la tap con")