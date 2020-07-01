class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h) >> 1
            nm = nums[m]
            nh = nums[h]
            if nm == nh:
                h -= 1
                continue
            elif nm > nh:
                l = m + 1
            else:
                h = m
        return nums[l]
