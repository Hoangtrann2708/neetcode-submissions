class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for i in range (len(nums)):
            res[i] = prefix
            prefix *= nums[i] # prefix = prefix * nums[i] ( prefix = 1* nums[0]= 1* 6)

        postfix =1
        for i in range (len(nums)-1, -1, -1):
            res[i] *= postfix  #  left product *  right product  
            postfix *= nums[i]

        return res



              