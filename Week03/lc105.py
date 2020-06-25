class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(pl, pr, il, ir):
            if pl > pr:
                return None
            val = preorder[pl]
            imid = t[val]
            ilen = imid - il
            node = TreeNode(val)
            node.left = dfs(pl + 1, pl + ilen, il, imid - 1)
            node.right = dfs(pl + ilen + 1, pr, imid + 1, ir)
            return node
        t = {v: i for i, v in enumerate(inorder)}
        n = len(preorder)
        return dfs(0, n - 1, 0, n - 1)
