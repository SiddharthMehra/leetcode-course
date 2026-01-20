class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        numSet = set(nums)

        for n in numSet:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length+=1
                
                ans = max(ans, length)
        
        return ans
