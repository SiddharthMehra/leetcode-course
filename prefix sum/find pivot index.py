class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0

        for i, num in enumerate(nums):
            if leftSum == (total - (leftSum + num)): #calculate left and right sum not including the current number
                return i
            leftSum+=num
        
        return -1

        