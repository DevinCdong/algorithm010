class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i, x in enumerate(nums):
            if i > far:
                return False
            far = max(far, i + x)
        return True
