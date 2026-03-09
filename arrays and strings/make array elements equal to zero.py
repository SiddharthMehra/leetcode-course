class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        ans = 0
        n = len(nums)

        def simulate(start, direction):
            arr = nums[:]
            i = start 
            d = direction

            while 0<=i<n:
                if arr[i] == 0:
                    i+=d
                
                else:
                    arr[i]-=1
                    d*=-1
                    i+=d
            return all(x == 0 for x in arr)
        
        for i in range(n):
            if nums[i] == 0:
                if simulate(i, 1):
                    ans+=1
                if simulate(i, -1):
                    ans+=1
        
        return ans
        
