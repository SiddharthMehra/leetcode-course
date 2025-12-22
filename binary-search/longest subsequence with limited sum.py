#sort nums + prefix sum + binary search

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()

        for i in range(1, len(nums)):
            nums[i]+=nums[i-1]
        
        ans = []

        for query in queries:
            index = bisect.bisect_right(nums, query)
            ans.append(index)
        
        return ans
