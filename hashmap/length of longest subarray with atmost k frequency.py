class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left, ans = 0, 0
        count = Counter(nums)
        hashmap = defaultdict(int)

        for right in range(len(nums)):
            hashmap[nums[right]]+=1
            while hashmap[nums[right]]>k:
                hashmap[nums[left]]-=1
                left+=1
            
            ans = max(ans, right-left+1)
        
        return ans


        