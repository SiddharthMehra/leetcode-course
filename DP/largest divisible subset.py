class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1]*len(nums)
        #to reconstruct the subset
        prev = [-1]*len(nums)
        maxi = 0

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0 and dp[i]<dp[j]+1:
                    dp[i]= dp[j]+1
                    #previous element of current element i is j
                    prev[i] = j
            
            #maxi is the index of the last element in the subset of sorted array
            if dp[i]>dp[maxi]:
                maxi = i
        
        #reconstruct using maxi, if it is -1, there is no parent/prev
        res = []
        i = maxi
        while i>=0:
            res.append(nums[i])
            i = prev[i]
        
        return res
        
