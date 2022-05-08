def branch_and_bound (lst, i, X, n):
    global Temp
    global Count
    global BestSolution
    if sum(Temp) > X:
        return
    for i in range(i, len(lst)):
        Temp.append(lst[i])
        if len(Temp) == n:
            if X - sum(Temp) >= 0:
                Count += 1
                if sum(Temp) > sum(BestSolution):
                    BestSolution = Temp.copy()
        else:
            branch_and_bound(lst, i + 1, X, n)
        Temp.pop()

if __name__ == '__main__':
  lst = [int(x) for x in input().split()]
  X, n = [int(x) for x in input().split()]
  Count = 0
  Temp = []
  BestSolution = []
  branch_and_bound(lst, 0, X, n)
  if Count != 0:
    print(Count)
    print(sum(BestSolution))
    print(BestSolution)
  else:
      print(0)