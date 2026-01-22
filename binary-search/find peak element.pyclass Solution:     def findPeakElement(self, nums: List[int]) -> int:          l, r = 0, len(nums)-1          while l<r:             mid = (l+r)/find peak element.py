class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1

        while l<r:
            mid = (l+r)//2

            #peak on mid or left of mid
            if nums[mid]>nums[mid+1]:
                r = mid
            #peak on right
            else:
                l = mid+1
        
        return l
