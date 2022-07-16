"""
Daily Coding Problem - Day 1

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

Thought Process
    - Write a nested for loop, and check if the sum equals to the target. Run time: O(n^2), SC: O(1)
    - Sort the list, and find target. TC: O(nlogn), SC: O(1) (or O(n) depending on the sorting algorithm
    - Loop through and save in hashmap: TC: O(n), SC: O(n)

    Using 3.
    Given a list: [3,1,5,6,1], k =7, the program should return True

    hashmap = {}
    Iteration 1
    val = 3, remaining = 4
    if remaining in
    Follow Up Question
    - What should be returned
    i) if the list is empty? False
    ii) if numbers that sum up to k  is not found? False
"""

def solution(arr, k):
    hashmap = {}

    for value in arr:
        remaining = k - value
        if remaining in hashmap:
            return True

        hashmap[value] = value
    return False

print(solution(arr= [3,5,6,12], k =0))
