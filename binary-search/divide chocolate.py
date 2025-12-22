class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
        left, right = 1, sum(sweetness)
        
        #maximise minimum partition sum
        def canDivide(minSweet):
            pieces, curr = 0, 0
            for sweet in sweetness:
                curr+=sweet
                if curr>=minSweet:
                    pieces+=1
                    curr = 0
            
            return pieces>=k+1
        
        while left<right:
            #to prevent infinite loop
            mid = (left+right+1)//2
            #check for a larger minimum
            if canDivide(mid):
                left = mid
            else:
                right = mid-1
        
        return left
        
        
