class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0 
        ans=0
        count = defaultdict(int)
        count[0]=1

        for num in nums:
            curr+=num

            if curr-k in count:
                ans+=count[curr-k] # for subarray sum k, current sum is curr, curr-(curr-k) = k
            count[curr]+=1
        
        return ans
        



