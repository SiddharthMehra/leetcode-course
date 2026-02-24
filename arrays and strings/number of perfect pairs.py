class Solution:
    def perfectPairs(self, nums: List[int]) -> int:

        arr = sorted(abs(x) for x in nums)

        n = len(arr)
        count = 0
        j = 0

        for i in range(n):
            while j<n and arr[j]<=2*arr[i]:
                j+=1
            count+=max(0, j-i-1)
        
        return count
        
