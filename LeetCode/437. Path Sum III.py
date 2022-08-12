# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, target):
            def solve(root, target):
                if root is None: return 0

                result = 0
                if root.val == target:
                    result += 1
                if root:
                    result += solve(root.left, target - root.val)
                    result += solve(root.right, target - root.val)
                return result

            if root is None: return 0
            return dfs(root.left, targetSum) + dfs(root.right, targetSum) + solve(root, targetSum)

        return dfs(root, targetSum)
