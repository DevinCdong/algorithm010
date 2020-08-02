学习笔记

### 排序 -- 归并
```
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
```


### 排序 -- 快排
```
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def qs(start, end):
            if start >= end:
                return
            m = partition(start, end)
            qs(start, m - 1)
            qs(m + 1, end)

        def sw(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def partition(start, end):
            i, j = start, end
            piv = nums[start]
            while i < j:
                while i < j and nums[j] > piv:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= piv:
                    i += 1
                nums[j] = nums[i]
            nums[i] = piv
            return i 
            
            slow = start
            piv = nums[end]
            for fast in range(start, end):
                if nums[fast] <= piv:
                    if fast > slow:
                        sw(fast, slow)
                    slow += 1
            sw(slow, end)
            return slow

        qs(0, len(nums) - 1)
        return nums
```
