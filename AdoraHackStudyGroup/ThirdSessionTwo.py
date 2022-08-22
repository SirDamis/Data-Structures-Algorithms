"""
Min Note
"""
def solution(n):
    count = 0
    if n > 9:
        count += (n//9)
        remainder = n%9
        if remainder: count += 1
        return count
    return 1
print(solution(8121))
