class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        ans , count = 0, 0
        for w in weight:
            if ans + w<=5000:
                ans+=w
                count+=1
        
        return count
            
        
