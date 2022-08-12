# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(res, path, target, node):
            if node:
                if not node.left and not node.right and target == node.val:
                    path += [node.val]
                    res.append(path)
                    return
                dfs(res, path + [node.val], target - node.val, node.left)
                dfs(res, path + [node.val], target - node.val, node.right)

        res = []
        dfs(res, [], targetSum, node=root)
        return res

