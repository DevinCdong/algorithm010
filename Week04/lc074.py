class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0: return False
        m = len(matrix[0])
        if m == 0: return False
        i, j = 0, m - 1
        while i < n and j >= 0:
            mij = matrix[i][j]
            if mij == target:
                return True
            elif mij > target:
                j -= 1
            else:
                i += 1
        return False
