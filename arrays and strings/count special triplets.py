from collections import defaultdict

class Solution:
    def specialTriplets(self, nums):

        mod = 10**9+7
        right, left = defaultdict(int), defaultdict(int)

        for num in nums:
            right[num]+=1
        
        result = 0

        for num in nums:
            right[num]-=1
            target = 2*num
            left_count = left[target]
            right_count = right[target]

            result = (result + left_count * right_count) % mod

            left[num]+=1
        
        return result
