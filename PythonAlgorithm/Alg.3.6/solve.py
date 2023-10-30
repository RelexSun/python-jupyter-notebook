def selectionsort(n, s) :
    cnt = 0
    for i in range(n - 1) :
        minv, minj = s[i], i
        for j in range(i + 1, n) :
            if s[j] < minv :
                minv, minj = s[j], j
        if i != minj :
            s[i], s[minj] = s[minj], s[i]
            cnt += 1
    return cnt

N = int(input())
S = list(map(int, input().split()))
print(selectionsort(N, S))