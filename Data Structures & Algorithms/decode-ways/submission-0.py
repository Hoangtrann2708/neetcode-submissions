class Solution:
    def numDecodings(self, s: str) -> int:
        n =len(s)
        dp = {n: 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0" :
                return 0
            ret= 0
            ret += dfs(i+1)
            if i+1 <n and 10<= int( s[i:i+2])<=26:
                ret+= dfs(i+2)
            dp[i]= ret
            return ret
        return dfs(0)

                


                
                
