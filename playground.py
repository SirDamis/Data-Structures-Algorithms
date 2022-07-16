"""
You are given a function:-
f(n) = 3*n +1, when n is odd,
f(n) = n/2, when n is even

Find the minimum number of steps to reach 1
"""

def solve(n):
    steps = 0
    if n == 1:
        return
    else:
        while int(n) > 1:
            print(n)
            if n % 2 == 1:
                n = 3*n + 1
            else:
                n = n/ 2
            steps += 1
    return steps

def solve2(n):
    maxNum = 0
    for i in range(1, n+1):
        maxNum = i if max(solve(i), maxNum)
    return maxNum


print(solve2(3))
