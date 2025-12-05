class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0

        for key, value in Counter(nums).items():
            if value == 1:
                ans+=key
        
        return ans