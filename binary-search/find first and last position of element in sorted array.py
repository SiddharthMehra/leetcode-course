class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.findBound(nums, target, True)
        if lower_bound == -1:
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)

        return [lower_bound, upper_bound]
    
    def findBound(self, nums, target, isLeftBound):
        n = len(nums)
        begin, end = 0, n-1
        while begin<=end:
            mid = (begin + end)//2

            if nums[mid] == target:
                if isLeftBound:
                    #leftmost instance is mid
                    if mid == begin or nums[mid-1]<target:
                        return mid
                    
                    #target is on the left side 
                    end = mid-1
                
                else:

                    if mid == end or nums[mid+1]>target:
                        return mid
                    
                    #search on the right side
                    begin = mid+1
            
            elif nums[mid]>target:
                end = mid-1
            else:
                begin = mid+1
        
        return -1
                    

