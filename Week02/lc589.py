"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        s = [(0, root)]
        res = []
        while s:
            flag, node = s.pop()
            if not node: continue
            if not flag:
                for ch in node.children[::-1]:
                    s.append((0, ch))
                s.append((1, node))
            else:
                res.append(node.val)
        return res
