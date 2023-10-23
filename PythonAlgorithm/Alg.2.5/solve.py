def perm(i, n, s) :
    if i == n - 1 :
        print("".join(s))
    else :
        for j in range(i, n) :
            s[i], s[j] = s[j], s[i]
            perm(i + 1, n, s)
            s[i], s[j] = s[j], s[i]
            
            
N = int(input())
S = [chr(ord('A') + i) for i in range(N)]
perm(0, N, S)