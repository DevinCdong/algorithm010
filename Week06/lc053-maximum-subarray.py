class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = 0
        res = -1e10
        for n in nums:
            dp = max(dp, 0) + n
            res = max(res, dp)
        return res
