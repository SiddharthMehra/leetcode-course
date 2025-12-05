class Solution:
    def numSubarraysWithSum(self, A, S):

        def atMost(arr, s):

            if s<0:
                return 0
            left, res, total = 0, 0, 0

            for right, val in enumerate(arr):
                total+=val
                while total>s:
                    total-=arr[left]
                    left+=1
                res+=right-left+1
            
            return res
        
        return atMost(A, S) - atMost(A, S-1)
