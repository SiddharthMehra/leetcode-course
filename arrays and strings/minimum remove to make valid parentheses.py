class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        #first pass to calculate extra "(" and remove invalid ")"

        first_pass_chars = []
        balance, open_brackets = 0, 0
        for c in s:
            if c == "(":
                balance+=1
                open_brackets+=1
            
            if c == ")":
                #skip when brackets are already balanced
                if balance == 0:
                    continue
                balance-=1
            
            first_pass_chars.append(c)
        
        #remove the rightmost "("
        result = []
        open_to_keep = open_brackets - balance
        for c in first_pass_chars:
            if c == "(":
                open_to_keep-=1
                if open_to_keep<0:
                    continue
            
            result.append(c)
        
        return "".join(result)

        
