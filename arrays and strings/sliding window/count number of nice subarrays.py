# key pattern: exactly k odd numbers implies atMost(k)-atMost(k-1)

class Solution:
    def numberOfSubarrays(self, nums: List[int], k:int) -> int:

        return self.atMost(nums, k) - self.atMost(nums, k-1)

    def atMost(self, nums: List[int], k: int) -> int:
        window_size, subarrays, start = 0, 0, 0

        for end in range(len(nums)):
            window_size+=nums[end]%2
            while window_size>k:
                window_size-=nums[start]%2
                start+=1
            
            subarrays+=end-start+1
        
        return subarrays
                
            




    
