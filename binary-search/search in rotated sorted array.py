class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        left, right = 0, n-1

        while left<=right:
            mid = (left+right)//2

            if nums[mid]==target:
                return mid
            
            #left -> mid is sorted
            elif nums[mid]>=nums[left]:
                if target>=nums[left] and target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            
            #mid -> right is sorted
            else:
                if target<=nums[right] and target>nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
        
        return -1
            

            


                
