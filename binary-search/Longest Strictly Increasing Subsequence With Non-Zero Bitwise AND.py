class Solution:
    def lengthOfLIS(self, arr):
        lis = []
        for x in arr:
            pos = bisect_left(lis, x)
            if pos == len(lis):
                lis.append(x)
            
            else:
                lis[pos] = x
        
        return len(lis)

    def longestSubsequence(self, nums: List[int]) -> int:

        max_len = 0
        for bit in range(32):
            #group numbers together with a particular bit set
            filtered = [x for x in nums if x & (1<<bit)]
            if not filtered:
                continue
            
            max_len = max(max_len, self.lengthOfLIS(filtered))

        return max_len
        
