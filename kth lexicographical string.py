#combinatorics

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        #all possible total combinations
        total = 3* (2**(n-1))
        if k>total:
            return ""
        
        res=[]
        prev = ""

        for i in range(n):
            for ch in "abc":
                if ch == prev:
                    continue
                
                #remaining elements that can be formed, skip all strings starting with ch
                cnt = 2**(n-1-i)
                if k>cnt:
                    k-=cnt
                
                else:
                    res.append(ch)
                    prev = ch
                    break
        
        return "".join(res)
                
