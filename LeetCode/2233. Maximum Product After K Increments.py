import heapq


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while k > 0:
            minimum = heapq.heappop(nums)
            heapq.heappush(nums, minimum + 1)
            k -= 1

        result = 1
        for num in nums:
            result = (result * num) % (10 ** 9 + 7)
        return result
