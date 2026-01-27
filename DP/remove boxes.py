class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        n = len(boxes)
        memo = {}

        def dp(l, r, k):

            if l>r:
                return 0

            if (l, r, k) in memo:
                return memo[(l, r, k)]
            
            #merge consecutive boxes of the same colour at the start
            while l<r and boxes[l] == boxes[l+1]:
                l+=1
                k+=1
            
            #case 1 -> remove box[l] and k extra to the left
            res = (k+1) * (k+1) + dp(l+1, r, 0)

            #try to merge with future same coloured boxes
            for m in range(l+1, r+1):
                if boxes[m] == boxes[l]:
                    res = max(res, dp(l+1, m-1, 0) + dp(m, r, k+1))

            memo[(l, r, k)] = res
            return res
        
        return dp(0, n-1, 0)
