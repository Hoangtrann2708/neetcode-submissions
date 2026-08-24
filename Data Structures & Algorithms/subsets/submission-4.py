class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []                       # 1
        subset = []                    # 2
        def dfs(i):                    # 3
            if i == len(nums):         # 4
                res.append(subset[:])  # 5
                return                 # 6
            subset.append(nums[i])     # 7
            dfs(i + 1)                 # 8
            subset.pop()               # 9
            dfs(i + 1)                 # 10
        dfs(0)                         # 11
        return res   