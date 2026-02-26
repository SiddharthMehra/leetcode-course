class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:

        n = len(nums)

        prefixMax = [0] * n
        suffixMin = [0] * n

        prefixMax[0] = nums[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i-1], nums[i])
        
        suffixMin[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffixMin[i] = min(suffixMin[i+1], nums[i])
        
        count = 0

        for i in range(n):
            left_ok = (i==0 or prefixMax[i-1]<nums[i])
            right_ok = (i==n-1 or suffixMin[i+1]>nums[i])

            if left_ok and right_ok:
                count+=1
        
        return count
        
