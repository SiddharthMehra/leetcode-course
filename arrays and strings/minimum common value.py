class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        def binary_search(target, nums):
            left, right = 0, len(nums)-1

            while left<=right:
                mid = left + (right-left)//2

                if nums[mid]>target:
                    right = mid-1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    return True
            
            return False
        
        if len(nums1)>len(nums2):
            return self.getCommon(nums2, nums1) # binary search on larger array, iterate through smaller array
        
        for num in nums1:
            if binary_search(num, nums2):
                return num
        
        return -1
        

                
# time complexity: O(nlogn)