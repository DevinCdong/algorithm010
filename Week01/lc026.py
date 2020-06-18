class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        p = k
        n = len(nums)
        for i in range(k, n):
            if nums[p - k] != nums[i]:
                nums[p] = nums[i]
                p += 1
        return p
