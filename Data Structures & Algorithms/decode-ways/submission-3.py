class Solution:
    def numDecodings(self, s: str) -> int:
        n =len(s)
        dp = {n: 1} ## 226 , n = 3 => 3:1 decode empty "" = 1
        
        def dfs(i):
            if i in dp: ## if i = 3
                return dp[i] ## return 1
            if s[i] == "0" : 
                return 0
            ret= 0
            ret += dfs(i+1)  ## dfs0 ,dfs1, dfs2, dfs(3)=1
            ## sau khi dfs 3 = 1 quay ve dfs dfs2 ở đầu nhưng dòng ret += dfs(2+1) =dfs(3)= 1 (đã có kết quả ) nên đi tiếp xuống dòng if dưới để bắt đầu ghép ngược các cặp số 26 , 22
            if i+1 <n and 10<= int( s[i:i+2])<=26:
                ret+= dfs(i+2)
            dp[i]= ret # lưu dfs(i) để bt rằng từ index i đến cuối đã tạo được bn cặp 
            return ret
        return dfs(0)


"""this problems we can starting by give an example:
 226 : HOW MANY ways we could decode this numbers
 JUST SIMPLIFY IT , INSTEAD OF HOW MANY WAYS TO DECODE 226
  1. STARTING BY SPILIT "2" AND "26"
   => so according to convertBoard ("2"=B) then we only have 26 
   => keep spilit it => "2" =B , "6" = F
   => "226" BBF = 1 WAY 
    Following by this solution we could use dfs()
    dfs(i) == starting in this position"i" how many way could we encode the rest of the string 
    For example dfs(2) (THIS IS THE FIRST "2")
    SO HOW MANY WAY COULD WE ENCODE "26"
    => Dynamic Programming
"""
    #1 The FLOW : STARTING 
        # dfs(2)=> dfs(2) => dfs(6)

        # then come back merge 2 and 6 => "26" =Z and the first digit 2 as a single group, it is B  => BZ
        
        # AFTER THAT THE SECOND 2 AND THE FIRST 2 MERGE THEN IT WILL BECOME "22" AND "6" and 


    


   

 

                


                
                
