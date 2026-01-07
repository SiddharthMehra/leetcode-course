class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            #rest of the elements cannot sum to zero
            if nums[i]>0:
                break

            #to prevent duplicates
            if i==0 or nums[i-1]!=nums[i]:
                self.twoSumII(nums, i, res)
        
        return res
    
    def twoSumII(self, nums, i, res):
        lo, hi = i+1, len(nums)-1
        while lo<hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum<0:
                lo+=1
            elif sum>0:
                hi-=1
            
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo+=1
                hi-=1
                #to prevent duplicates
                while lo<hi and nums[lo]==nums[lo-1]:
                    lo+=1

            




