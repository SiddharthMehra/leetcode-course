class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:

        res = 0

        for l, r in queries:
            total_ops = 0
            curr = 1
            op_val = 1

            while curr<=r:
                start = max(curr, l)
                end = min(4 * curr-1, r)
                if start<=end:
                    total_ops+=(end-start+1) * op_val
                
                curr*=4
                op_val+=1
            
            res+=ceil(total_ops/2)
        
        return res
