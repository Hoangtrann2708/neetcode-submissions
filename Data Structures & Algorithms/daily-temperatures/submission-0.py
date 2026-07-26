class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                old_temp,old_index = stack.pop()
                res[old_index] = i - old_index
            
            stack.append((t,i))
        return res
