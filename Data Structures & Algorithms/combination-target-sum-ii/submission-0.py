class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res= []
        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            if i >= len(candidates) or total > target:
                return
            path.append(candidates[i])
            dfs(i+1, path, total+ candidates[i])
            path.pop()

            while i+1< len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, path, total)

        dfs(0,[],0)
        return res




                
                
        