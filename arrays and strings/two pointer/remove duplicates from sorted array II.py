class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i, j = 1, 1
        count = 1

        while i<len(nums):
            if nums[i] == nums[i-1]:
                count+=1
                #skip if more than 2
                if count>2:
                    i+=1
                    continue
            #reset count to 1
            else:
                count = 1
            
            nums[j] = nums[i]
            i+=1
            j+=1
        
        del nums[j:]
        return len(nums)




        
