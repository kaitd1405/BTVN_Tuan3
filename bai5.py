
def MyMathShower(*a) :
    tong=0
    hieu=2*a[0]
    tich=1
    for i in a:
        tong+=i
        hieu-=i
        tich*=i
    print(tong,tich,hieu)
MyMathShower(10, 4, 1, 1)
