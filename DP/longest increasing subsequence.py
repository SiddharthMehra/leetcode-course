#DP + binary search
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        subsequence = []

        for num in nums:
            i = bisect_left(subsequence, num)

            #if num if greater than every other element in sub
            if i == len(subsequence):
                subsequence.append(num)
            
            else:
                subsequence[i] = num
        
        return len(subsequence)
            
            


