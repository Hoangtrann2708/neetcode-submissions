class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        ret = 0
        total = 0
        for num in nums:
            total += num
            needed= total-k
            ret+= count.get(needed,0) 
            count[total] = count.get(total,0)+1
        return ret
        