class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(cur):
            if len(cur) == n:
                res.append(cur[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = 1
                cur.append(nums[i])
                dfs(cur)
                cur.pop()
                used[i] = 0

        res = []
        nums.sort()
        n = len(nums)
        used = [0] * n
        dfs([])
        return res
