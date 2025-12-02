class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        averages = [-1]*len(nums)
        if k==0:
            return nums
        
        window_size = 2*k+1
        n = len(nums)

        if window_size>n:
            return averages
        
        window_sum = sum(nums[:window_size])
        averages[k] = window_sum//window_size

        for i in range(window_size, n):
            window_sum = window_sum - nums[i-window_size]+nums[i]
            averages[i-k] = window_sum//window_size
        
        return averages