#sorting to break early if possible

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]

        def dfs(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            #tracks duplicates at the same level

            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                if candidates[i]>remaining:
                    break
                
                path.append(candidates[i])
                dfs(i+1, path, remaining-candidates[i])
                path.pop()

                prev = candidates[i]
            
        dfs(0, [], target)
        return res
