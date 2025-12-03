class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        setOfNumbers = set(arr)
        count=0
        
        for x in arr:
            if (x+1) in setOfNumbers:
                count+=1
        
        return count
        