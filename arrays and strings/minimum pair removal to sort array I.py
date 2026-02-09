class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        num = nums[:]
        operations = 0

        def non_decreasing(arr):

            for i in range(1, len(arr)):
                if arr[i]<arr[i-1]:
                    return False
            return True
        
        while not non_decreasing(num):
            min_sum = float('inf')
            index = 0

            for i in range(len(num)-1):
                pair_sum = num[i] + num[i+1]
                if pair_sum<min_sum:
                    min_sum = pair_sum
                    index = i
            
            num[index]+=num[index+1]
            del num[index+1]

            operations+=1
        return operations

        
