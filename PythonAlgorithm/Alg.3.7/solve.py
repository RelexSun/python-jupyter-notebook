def insertionsort(n, s) :
    cnt = 0
    for i in range(1, n) :
        j, val = i - 1, s[i]
        cnt += 1
        while j >= 0 and s[j] > val :
            s[j + 1] = s[j]
            j -= 1
            cnt += 1
        s[j + 1] = val
    return cnt

N = int(input())
S = list(map(int, input().split()))
print(insertionsort(N, S))