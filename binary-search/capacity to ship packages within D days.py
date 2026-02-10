class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left, right = max(weights), sum(weights)
        while left<right:
            mid, need, curr = (left+right)//2, 1, 0
            for w in weights:
                if curr + w> mid:
                    need+=1
                    curr = 0
                curr+=w
            
            if need>days:
                left = mid+1
            else:
                right = mid
            
        return left
            
