def bubblesort(n, s) :
    cnt = 0
    for i in range(n - 1) :
        for j in range(n - 1 - i) :
            if s[j] > s[j + 1] :
                s[j], s[j + 1] = s[j + 1], s[j] 
                cnt += 1
        print(s, cnt)
    return cnt

N = int(input())
S = list(map(int, input().split()))
print(bubblesort(N, S))