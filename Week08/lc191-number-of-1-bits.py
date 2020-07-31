class Solution:
    def hammingWeight(self, n: int) -> int:
        # 更少循环
        cnt = 0
        while n:
            cnt += 1
            n &= (n - 1)
        return cnt
        
        
        cnt = 0
        while n:
            cnt += n & 1
            n >>= 1
        return cnt
