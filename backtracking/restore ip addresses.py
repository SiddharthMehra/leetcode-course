class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        if len(res)>12:
            return res
        
        def backtrack(i, dots, currIp):
            if dots == 4 and i == len(s):
                #dont include the last dot
                res.append(currIp[:-1])
                return
            
            if dots>4:
                return
            
            #to prevent out of bounds
            for j in range(i, min(i+3, len(s))):
                #leading characters cannot be equal to 0 
                if int(s[i:j+1]) < 256 and (i==j or s[i]!="0"):
                    backtrack(j+1, dots+1, currIp + s[i:j+1] + ".")
        
        backtrack(0, 0, "")
        return res

