class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0]*(2*n)
        for i in range(n):
            ret[i],ret[i+n]= nums[i], nums[i]
        return ret
        