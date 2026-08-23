class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        perms = self.permute(nums[1:])
        res =[]
        for perm in perms:
            for i in range (len(perm)+1):
                res.append(perm[:i] + [nums[0]]+ perm[i:])
        return res