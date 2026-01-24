class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        n = len(nums)
        ans = list()

        for i in range(n-k+1):
            #k element sliding window
            cnt = Counter(nums[i:i+k])

            #first sort in decreasing order of frequency and then in decreasing order of key
            freq = sorted(cnt.items(), key = lambda item: (-item[1], -item[0]))
            xsum = sum(key * value for key, value in freq[:x])
            ans.append(xsum)

        return ans        
