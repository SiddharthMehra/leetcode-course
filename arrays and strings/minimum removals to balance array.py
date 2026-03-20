class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:

        n = len(nums)
        nums.sort()

        ans = n
        right = 0

        for left in range(n):
            while right<n and nums[right]<=nums[left] * k:
                right+=1
            
            #maximise right - left which is the length of the valid array to minimise the number of removals
            ans = min(ans, n - (right-left))
        
        return ans
        
