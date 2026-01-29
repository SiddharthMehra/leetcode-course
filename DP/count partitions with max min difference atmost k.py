class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        
        #dp with sliding window
        n = len(nums)
        mod = 10**9+7

        dp = [0]*(n+1)
        prefix = [0] * (n+1)
        min_q = deque()
        max_q = deque()

        dp[0] = 1
        prefix[0] = 1
        left = 0

        for right in range(n):
            while max_q and nums[max_q[-1]]<=nums[right]:
                max_q.pop()
            max_q.append(right)

            while min_q and nums[min_q[-1]]>=nums[right]:
                min_q.pop()
            min_q.append(right)

            #shring window if max - min>k

            while max_q and min_q and nums[max_q[0]] - nums[min_q[0]]>k:
                if max_q[0] == left:
                    max_q.popleft()
                
                if min_q[0] == left:
                    min_q.popleft()
                
                left+=1

            if left>0:
                dp[right+1] = (prefix[right] - prefix[left-1] ) %mod
            else:
                dp[right+1] = prefix[right] % mod
            
            prefix[right+1] = (prefix[right] + dp[right+1]) % mod
             
    
        return dp[n]

        
