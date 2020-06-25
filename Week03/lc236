# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node or node == p or node == q:
                return node
            ll = dfs(node.left)
            rr = dfs(node.right)
            if ll and rr:
                return node
            else:
                return ll if ll else rr
        return dfs(root)

