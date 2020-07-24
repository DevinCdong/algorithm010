class Solution:
    dirs = [(i, j) for i in range(-1, 2) for j in range(-1, 2)
            if not(i != 0 and j != 0) and not (i == 0 and j == 0)]
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        end = "#"
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node[end] = word
        
        def dfs(i, j, node):
            c = board[i][j]
            if c not in node:
                return
            sub = node[c]
            if end in sub:
                res.append(sub.pop(end))
            if not sub:
                node.pop(c)
            board[i][j] = "$"
            for di, dj in self.dirs:
                ii, jj = i + di, j + dj
                if not (0 <= ii < n and 0 <= jj < m and not board[ii][jj] == "$"):
                    continue
                dfs(ii, jj, sub)
            board[i][j] = c

        n = len(board)
        m = len(board[0])
        res = []
        for x in range(n):
            for y in range(m):
                dfs(x, y, trie)
        return res
