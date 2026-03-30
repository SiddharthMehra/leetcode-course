class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:

        n = len(nums)

        memo = [[[None] * (op2+1) for _ in range(op1+1)] for _ in range(n)]

        def dp(i, o1, o2):

            if i ==n:
                return 0
            
            if memo[i][o1][o2] is not None:
                return memo[i][o1][o2]
            
            x = nums[i]

            # 1: do nothing
            res = x + dp(i+1, o1, o2)

            # 2 -> operation 1
            if o1>0:
                val = math.ceil(x/2)
                res = min(res, val + dp(i+1, o1 - 1, o2))
            
            if o2>0 and x>=k:
                val = x - k
                res = min(res, val + dp(i+1, o1, o2-1))
            
            #both operations 
            #op1 -> op2
            if o1>0 and o2>0:
                val1 = math.ceil(x/2)
                if val1>=k:
                    val1-=k
                    res = min(res, val1 + dp(i+1, o1-1, o2-1))
                
                #op2 -> op1
                if x>=k:
                    val2 = x-k
                    val2 = math.ceil(val2/2)
                    res = min(res, val2 + dp(i+1, o1 -1, o2-1))
            
            memo[i][o1][o2] = res
            return res
        
        return dp(0, op1, op2)


        
