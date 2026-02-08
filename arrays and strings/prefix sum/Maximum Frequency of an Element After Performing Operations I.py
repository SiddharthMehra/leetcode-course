class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:

        n = max(nums)
        count = [0] * (n+1)
        for num in nums:
            count[num]+=1
        
        preSum = [0]
        for i in range(n+1):
            preSum.append(preSum[-1] + count[i])
        
        ans = 0

        for i in range(n+1):
            left = preSum[i] - preSum[max(0, i-k)]
            right = preSum[min(n+1, i+k+1)] - preSum[i+1]
            curr = count[i] + min(numOperations, left+right)
            ans = max(ans, curr)
        
        return ans
            

        
