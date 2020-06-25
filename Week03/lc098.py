# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return True
            if not dfs(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            if not dfs(node.right):
                return False
            return True
        self.prev = -1e10
        return dfs(root)


        def dfs(node, ll, rr):
            if not node:
                return True
            if not ll < node.val < rr:
                return False
            if not (dfs(node.left, ll, node.val) and dfs(node.right, node.val, rr)):
                return False
            return True
        return dfs(root, -1e10, 1e10)
            
