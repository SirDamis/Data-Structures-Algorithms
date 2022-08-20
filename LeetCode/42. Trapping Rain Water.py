class Solution:
    def trap(self, height: List[int]) -> int:
        #         # Approach 1:  TC: O(N), SC: O(N)
        #         # Using leftprefix and rightprefix
        #         n = len(height)
        #         initial = height[0]
        #         leftprefix = [initial]*n
        #         for idx in range(1, n):
        #             if height[idx] > leftprefix[idx-1]:
        #                 leftprefix[idx] = height[idx]
        #             else:
        #                 leftprefix[idx] = leftprefix[idx-1]

        #         last = height[n-1]
        #         rightprefix = [last]*n
        #         for idx in range(n-2, -1, -1):
        #             if height[idx] > rightprefix[idx+1]:
        #                 rightprefix[idx] = height[idx]
        #             else:
        #                 rightprefix[idx] = rightprefix[idx+1]
        #        water = 0
        #        for idx in range(n):
        #            water += (min(leftprefix[idx], rightprefix[idx]) - height[idx])
        #        return water

        # Approach 2:
        # Using Two Pointer
        n = len(height)
        left, right = 0, n - 1
        leftmax, rightmax = height[0], height[n - 1]
        water = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    water += (leftmax - height[left])
                left += 1
            else:
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    water += (rightmax - height[right])
                right -= 1
        return water
