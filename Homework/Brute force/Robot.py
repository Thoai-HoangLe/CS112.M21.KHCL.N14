def Convert(s, m, n):
    x, y = 0, 0
    for i in range(len(s)):
        if s[i] == 'L':
            y -= 1
        elif s[i] == 'R':
            y += 1
        elif s[i] == 'U':
            x -= 1
        elif s[i] == 'D':
            x += 1
        if m + x <= 0 or n + y <= 0 or x >= m or y >= n:
            return False
    return True

if __name__ == '__main__':
    m, n = map(int,input().split())
    s = input()
    if Convert(s, m, n):
        print('Safe')
    else: print('Unsafe') 
