"""
We can determine how "out of order" an array is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j.
That is, an element appears after a larger element.
Given an array, count the number of inversions it has. Do this faster than O(n^2) time.
Assumption: Each element is distinct.

Example: Input: [2,4,1,3,5], Output: 3, (2,1), (2,1), (4,1)
"""
import unittest


def countInversionBruteForce(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

def countInversionMergeSort(arr):
    return
def countInversionFemwickAlgorithm(arr):
    return

class CountInversionTest(unittest.TestCase):
    def testbruteforce(self):
        result = countInversionBruteForce([2, 4, 1, 3, 5])
        self.assertEqual(result, 3)

        result = countInversionBruteForce([0,1,2,3,4])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
