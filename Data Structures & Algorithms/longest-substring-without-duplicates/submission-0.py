class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Charset= set()
        l =0 
        res= 0
        for r in range (len(s)):
            while s[r] in Charset:
                Charset.remove(s[l])
                l+=1
            Charset.add(s[r])
            res= max(res,r-l+1)
        return res


        