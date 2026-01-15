class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)

        #delete useless elements less than 0 or greater than equal to n
        for i in range(len(nums)):
            if nums[i]<0 or nums[i]>=n:
                nums[i] = 0
        
        #mark how many times each element from 1 to n has occured
        for i in range(len(nums)):
            nums[nums[i] % n]+=n
        
        #if it hasnt ocurred a single time, nums[i]/n will be 0
        for i in range(1, len(nums)):
            if nums[i]// n == 0:
                return i
        
        return n


