class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(curr, i):
            ans.append(curr[:])

            for j in range(i, len(nums)):
                if j>i and nums[j] == nums[j-1]:
                    continue
                
                curr.append(nums[j])
                backtrack(curr, j+1)
                curr.pop()
            
        
        ans = []
        backtrack([], 0)
        return ans
