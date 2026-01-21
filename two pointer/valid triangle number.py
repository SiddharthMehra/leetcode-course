class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n= len(nums)
        count = 0

        for i in range(n-1, -1, -1):
            l, r = 0, i-1
            while l<r:
                #all values of l from l+1 to r would word, decrement r
                if nums[l] + nums[r]>nums[i]:
                    count+=(r-l)
                    r-=1
                else:
                    #too small, increase l
                    l+=1
        
        return count
                
