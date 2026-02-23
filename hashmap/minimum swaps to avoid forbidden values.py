class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:

        count = 0
        n = len(nums)
        maxi = 0
        num_map = Counter()
        forbidden_map = Counter()
        matching = Counter()

        for i in range(n):
            if nums[i] == forbidden[i]:
                count+=1
                matching[nums[i]]+=1
                maxi = max(maxi, matching[nums[i]])
            
            num_map[nums[i]]+=1
            forbidden_map[forbidden[i]]+=1
        
        #no amount of swaps are enough
        for key, value in num_map.items():
            if value > n - forbidden_map.get(key, 0):
                return -1
        
        return max(maxi, (count+1)//2)
        
