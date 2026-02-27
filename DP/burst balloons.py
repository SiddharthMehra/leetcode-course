class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        #burst "k" balloon last between left and right
        nums = [1] + nums + [1]
        n = len(nums)
        memo = {}

        def dfs(left, right):
            #no balloons in between
            if right - left == 1:
                return 0
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            max_coins = 0

            #try bursting "k" last

            for k in range(left+1, right):
                coins = (dfs(left, k) + dfs(k, right) + nums[left] * nums[k] * nums[right])
                max_coins = max(max_coins, coins)
            
            memo[(left, right)] = max_coins
            return max_coins
        
        return dfs(0, n-1)

        
