class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        dic[0]=-1  # to consider subarrays from the start
        ans, count = 0, 0

        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count-=1
            
            if count in dic:
                ans = max(ans, i-dic[count]) # dic[count] is the index where the sum is the same as current sum, so difference between the sum at i and sum at dic[count] is 0
            else:
                dic[count]=i
        
        return ans
        
        