学习笔记

@ 排序 -- 归并
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mg(start, end):
            if start >= end:
                return
            m = (start + end) >> 1
            mg(start, m)
            mg(m + 1, end)
            i = j = 0
            l, r = m - start, end - m - 1
            while i <= l and j <= r:
                if nums[start + i] <= nums[m + 1 + j]:
                    aux[start + i + j] = nums[start + i]
                    i += 1
                else:
                    aux[start + i + j] = nums[m + 1 + j]
                    j += 1
            while i <= l:
                aux[start + i + j] = nums[start + i]
                i += 1
            while j <= r:
                aux[start + i + j] = nums[m + 1 + j]
                j += 1
            nums[start: end + 1] = aux[start: end + 1]

        n= len(nums)
        aux = [0] * n
        mg(0, n - 1)
        return nums
                
