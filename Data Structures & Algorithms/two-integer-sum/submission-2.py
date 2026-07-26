class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMAP ={}
        for i, n in enumerate (nums):
            diff = target - n
            if diff in prevMAP:
                return [prevMAP[diff],i]
            prevMAP[n] = i
        return