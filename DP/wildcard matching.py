class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        #remove duplicate '*'
        new_p = []
        for c in p:
            if not new_p or c!='*' or new_p[-1]!='*':
                new_p.append(c)
        
        p = "".join(new_p)
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            #if pattern is exhausted, string must also be exhausted
            if j == len(p):
                ans = (i == len(s))
            
            #if string is exhausted, remaining pattern must all be "*"
            elif i == len(s):
                ans = all( c == '*' for c in p[j:])
            
            #characters match, move both string and pattern forward
            elif p[j] == s[i] or p[j] == '?':
                ans = dp(i+1, j+1)
            
            elif p[j] == '*':
                # '*' matches empty or more characters
                ans = dp(i+1, j) or dp(i, j+1)
            
            else:
                ans = False
            
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)
