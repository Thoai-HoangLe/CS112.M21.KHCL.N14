def MaxSubArraySum(a, size):
    max_so_far = a[0]
    max_ending_here = 0
    for i in range(0,size):
        max_ending_here = max_ending_here + a[i]
        if(max_so_far < max_ending_here):
            max_so_far = max_ending_here
        if(max_ending_here < 0):
            max_ending_here = 0
    return max_so_far

if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split())) 
    print(MaxSubArraySum(a,N))     



