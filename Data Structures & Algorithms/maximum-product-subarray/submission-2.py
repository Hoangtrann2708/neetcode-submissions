class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1,1
        ret = nums[0]
        for n in nums:
            temp = curMax
            curMax= max(curMax*n, n, curMin*n)
            curMin = min(curMin*n, n , temp*n)
            ret = max(ret,curMax)
        return ret