def Different(a,b):
    x = [i for i in a if i not in b]
    return x
print(Different([1,2,3],[1,'2',3]))