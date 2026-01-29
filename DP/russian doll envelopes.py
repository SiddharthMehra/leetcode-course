class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        #sort increasing in width and decreasing in height. if width same sort in decreasing order of height
        envelopes.sort(key = lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []

            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    #already there in array
                    dp[idx] = nums[i]
                
            return len(dp)
        
        return lis([i[1] for i in envelopes])
        
