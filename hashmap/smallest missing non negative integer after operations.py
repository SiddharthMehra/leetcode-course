class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:

        count = Counter([num % value for num in nums])

        mex = 0
        while True:
            remainder = mex%value
            if count[remainder]>0:
                count[remainder]-=1
                mex+=1
            else:
                return mex
        
