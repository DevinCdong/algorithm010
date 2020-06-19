# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        s = [(0, root)]
        res = []
        while s:
            flag, node = s.pop()
            if not node: continue
            if flag == 0:
                s.append((0, node.right))
                s.append((1, node))
                s.append((0, node.left))
            else:
                res.append(node.val)
        return res
