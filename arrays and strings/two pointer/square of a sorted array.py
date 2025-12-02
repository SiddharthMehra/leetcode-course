class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos = n-1
        l, r = 0, n-1
        res=[0]*(n)
        
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                res[pos] = nums[l]*nums[l]
                l+=1
            else:
                res[pos] = nums[r]*nums[r]
                r-=1
            pos-=1
        
        return res
        

#Time Complexity: O(N)
#Space Complexity: O(1)