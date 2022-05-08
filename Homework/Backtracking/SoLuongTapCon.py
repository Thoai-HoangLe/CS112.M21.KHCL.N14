from itertools import count


n, d = map(int,input().split())
lst = [int(x) for x in input().split()]

def SubSetSum(lst, sum, d):
    global count
    if sum == d:
        count += 1
    elif sum < d and len(lst) > 0:
        SubSetSum(lst[1:], sum, d)
        SubSetSum(lst[1:], sum + lst[0], d)

count = 0
SubSetSum(lst, 0, d)
print(count)