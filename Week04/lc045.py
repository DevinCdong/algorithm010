class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        end = 0
        far = 0
        for i, x in enumerate(nums[:-1]):
            far = max(far, i + x)
            if i == end:
                res += 1
                end = far
        return res
