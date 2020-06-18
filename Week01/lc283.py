class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        n = len(nums)
        for r in range(n):
            if nums[r] != 0:
                if l != r:
                    nums[l] = nums[r]
                l += 1
                
        for i in range(l, n):
            nums[i] = 0
        
