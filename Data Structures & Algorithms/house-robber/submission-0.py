class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) ## so at first we need have len of list
        if n == 1: ## if the list has only 1 vari => 
            return nums[0]
        dp = [0]*n ## we need a dp array => [0,0,0,0]
        dp[0] = nums[0] # dp[i] means the largest values we could have from 0 to i , our base case is i = 0 => LARGET PRICE WE COULD HAVE FROM 0 TO 0 IS NUMS[0]
        dp[1] = max(nums[0],nums[1])
        "for example if we have only 2 house [ 5,10]=> ofc we will take the second"
        for i in range (2,n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[n-1]
        

        

        
        