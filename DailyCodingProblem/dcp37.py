"""
Daily Coding Problem - Day 37

The power set of a set is the subset of all its subsets. Write a function that given a set, generates a
power set
Example: Given the set {1,2,3}, it should return {{}, {1}, {2}, {3}, {1, 2} {1,3}, {2,3}, {1,2,3}}

"""

def solution(setOfNumbers):
    def dfs(nums, path, ret):
        res.append(path)
        for idx, num in enumerate(nums):
            dfs(nums[idx+1:], path+[nums[idx]], res)

    res = []
    dfs(setOfNumbers, [], res)
    return res

print(solution([1,2,3]))
