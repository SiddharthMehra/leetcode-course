class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        ans = 0

        for right in range(len(nums)):
            for left in range(right):
                diff = nums[right] - nums[left]
                #take the max by extending the current sequence at left or current at right
                dp[(right, diff)] = max(dp[(left, diff)]+1, dp[(right, diff)] )
            
                ans = max(ans, dp[(right, diff)] )

        #ans stores number of extensions add 1 for the original number also
        return ans+1       
