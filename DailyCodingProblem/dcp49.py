"""
Given an array of numbers, find the maximum sum of contiguous subarray of the array.
Input: [34, -50, 42, 14, -5, 86], Output: 137 -> [42, 14, -5, 86]
"""
def maximumSubarray(arr):
    maximum = arr[0]
    currSum = 0
    for num in arr:
        if currSum < 0:
            currSum = 0
        currSum += num
        maximum = max(maximum, currSum)
    return maximum


import unittest
class CodeTest(unittest.TestCase):
    def testI(self):
        arr = [34, -50, 42, 14, -5, 86]
        maximum = maximumSubarray(arr)
        self.assertEqual(maximum, 137)
    def testII(self):
        arr = [34, -50]
        maximum = maximumSubarray(arr)
        self.assertEqual(maximum, 34)
    def testIII(self):
        arr = [0]
        maximum = maximumSubarray(arr)
        self.assertEqual(maximum, 0)
if __name__ == '__main__':
    unittest.main()
