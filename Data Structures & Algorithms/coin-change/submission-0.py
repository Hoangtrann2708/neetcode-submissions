class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] *(amount+1) 
            # [amount +1] la cac gia tri cua toan bo cua list con (amount+1 ) la so luong ptu trong array
        dp[0]=0
        for i in range (1,amount+1):
            for c in coins :
                if i -c >=0:
                    dp[i]= min(dp[i],1 + dp[i-c])
        return dp[amount] if dp[amount]!= amount+1 else -1
                
