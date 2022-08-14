"""
Given an array of integers, return a new array such that each element at index i of the new array is the
product of all the numbers in the original array except at i.
Example:
    input: [1, 2, 3, 4, 5]
    output: [120, 60, 40, 30, 24]
"""
def solution(arr):
    """
    Using division
    :param arr:
    :return arr:
    """
    product = 1
    for num in arr:
        product *= num
    for idx, num in enumerate(arr):
        arr[idx] = product//arr[idx]
    return arr

def solutionWithoutDivision(arr):
    """
    Without using division:
        Approach use prefix and postfix sum
    :param arr:
    :return arr:
    """
    output = [1]*len(arr)
    prefix = 1
    for i in range(len(arr)):
        print(prefix, arr[i])
        output[i] = prefix
        prefix *= arr[i]
    postfix = 1
    for i in range(len(arr)-1, -1, -1):
        output[i] *= postfix
        postfix *= arr[i]
    return output
arr = [1, 2, 3, 4, 5]
# print(solution(arr))
print(solutionWithoutDivision(arr))
