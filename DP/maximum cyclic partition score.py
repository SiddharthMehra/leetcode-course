class Solution:

    def maximumProfit(self, prices, k):

        f = [[-inf] * 3 for _ in range(k+2)]
        for j in range(1, k+2):
            f[j][0] = 0
        for p in prices:
            for j in range(k+1, 0, -1):
                f[j][0] = max(f[j][0], max(f[j][1] + p, f[j][2] - p))
                f[j][1] = max(f[j][1], f[j-1][0] - p)
                f[j][2] = max(f[j][2], f[j-1][0] + p)
        return f[-1][0]
    
    def maximumScore(self, nums, k):
        max_i = nums.index(max(nums))
        ans1 = self.maximumProfit(nums[max_i:] + nums[:max_i], k)
        ans2 = self.maximumProfit(nums[max_i+1:] + nums[:max_i+1], k)
        return max(ans1, ans2)
        
