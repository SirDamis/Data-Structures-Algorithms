"""
Given an array of integers, find the first missing postive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

Example:
    Input: [3, 4, -1, 1], Output: 2
    Input:; [1, 2, 0], Output: 3
"""
def solution(nums):
    """

    :param arr: arr
    :return : int
    """
    nums.sort()
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0
    initial = 0
    for i in range(0, len(nums)):
        if nums[i] == 0:
            continue
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] - initial != 1:
            return initial + 1
        else:
            initial = nums[i]
    return nums[i] + 1
def solution2(nums):
    """
    TodoSolution with constant space and n time complexity
    :param nums:
    :return:  int
    """
    return

arr = [1, 2, 0, -3, -3]
print(solution(arr))
print(solution2(arr))
