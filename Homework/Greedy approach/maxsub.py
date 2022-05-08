n = int(input())
lst = [int(x) for x in input().split()]
lst1 = [x for x in lst if x < 0]
lst2 = [x for x in lst if x > 0]

def Tich(lst):
    tich = 1
    for i in range(len(lst)):
        tich *= lst[i]
    return tich

t1, t2 = Tich(lst1), Tich(lst2)
if t1 < 0:
    t1 //= max(lst1)
if len(lst) == 1:
    print(lst[0])
elif lst2:
    print(t1 * t2)
elif t1 > 0 and len(lst1) > 1:
    print(t1)
else: print(0)