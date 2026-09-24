class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIndex = 0
        resLen = 0
        for i in range(len(s)):
            l, r = i, i  # when the substring is odd
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIndex = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1  # when the substring is even
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIndex = l
                    resLen = r - l + 1
                l -= 1
                r += 1
        return s[resIndex : resIndex + resLen]

        """
        1.
        ababd
        a: a,ab,aba,abab,ababd =>5
        b: b, ba,bab,babd=>4
        ...
        d: d =>1


        0: n times 
        1: n-1 times
        ...
        n-1: 1 times

        : n +(n-1)+...+ 1 = n(n+1)/2 ~ n^2

        ababd => 2 pointer => Traverse whole substring => n

        Overall (n^2 * n) = n^3

        => We recognize that when we use a as an index to traverse "abab" then when b using as an index to traverse again it also use "bab" again 
        => "bab" repeat => Optimize
        => Explode from middle
         #abbba (01234)
         mid = b => set 2 pointers in b , then explode from that b
         so because b in the 2th index has already been a palindromic => keep explode left right
         so left pointer right now is on the first b whereas the right poiter on third position and they are also b but they dont need to care about the second b anymore
         silmutaneously , 2 'a' on the side also need to check each other and forget about 2 b beside those and the b in the middle
        """