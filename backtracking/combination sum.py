class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        def backtrack(curr, i, currSum):
            if currSum == target:
                ans.append(curr[:])
                return
            
            #you can use a number multiple times
            for j in range(i, len(candidates)):
                num = candidates[j]
                if currSum + num<=target:
                    curr.append(num)
                    backtrack(curr, j, currSum+num)
                    curr.pop()
        
        ans = []
        backtrack([], 0, 0)
        return ans
