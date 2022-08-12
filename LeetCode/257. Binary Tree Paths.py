# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(node, path, res):
            if node:
                if not node.left and not node.right:
                    path += str(node.val)
                    res.append(path)
                dfs(node.left, path + str(node.val) + "->", res)
                dfs(node.right, path + str(node.val) + "->", res)

        res = []
        dfs(root, "", res)
        return res
