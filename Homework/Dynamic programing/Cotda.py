n = int(input())
lst = [int(x) for x in input().split()]
M = [0]*n

if n > 2:
    M[1] = abs(lst[1] - lst[0])
    for i in range(2, n):
        M[i] = min(abs(lst[i] - lst[i- 2]) + M[i-2], abs(lst[i] - lst[i-1]) + M[i-1])  
    print(M[n - 1]) 
elif n == 2:
    print(abs(lst[1] - lst[0]))	
else: print(0)