class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1,1
        ret = nums[0]
        for n in nums:
            temp = curMax
            curMax = max(n,curMax*n, curMin*n)
            curMin = min(n,curMin*n, temp*n)
            ret = max(ret,curMax)
        return ret