class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        #in python max of "0" and "000" is "000"
        res = "0"

        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                res = max(res, num[i: i+3])
        
        return "" if res == "0" else res
