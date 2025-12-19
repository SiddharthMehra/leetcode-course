class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        array = sorted(boxTypes, key = lambda x: -x[1])
        ans=0
        for box, unit in array:
            if box<=truckSize:
                ans+=box*unit
                truckSize-=box
            else:
                ans+=truckSize*unit
                break
        
        return ans
                
        
