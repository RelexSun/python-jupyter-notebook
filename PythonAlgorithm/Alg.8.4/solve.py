def solve(roman) :
    T = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    s = 0
    for i in range(len(roman) - 2) :
        if T[roman[i]] < T[roman[i+1]] :
            s -= T[roman[i]]
        else :
            s += T[roman[i]]

    s += T[roman[i+1]]
    return s + T[roman[-1]]

N = input()
print(solve(N))