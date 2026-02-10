class Solution:
    def checkValidString(self, s: str) -> bool:

        open_count, closed_count = 0, 0
        length = len(s) - 1

        #traverse the string from both ends simultaneously
        for i in range(length+1):
            if s[i] == "(" or s[i] == "*":
                open_count+=1
            #simulating the process of closing an open bracket
            else:
                open_count-=1
            
            if s[length-i] == ")" or s[length - i] == "*":
                closed_count+=1
            else:
                closed_count-=1
            
            if open_count<0 or closed_count<0:
                return False
        
    
        return True
