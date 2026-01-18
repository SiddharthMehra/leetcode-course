class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = defaultdict(int), defaultdict(int)

        for c in t:
            countT[c] = 1 + countT[c]
        
        #len(countT) gives the number of unique chars in T
        have, need = 0, len(countT)
        result, resultLength = [-1, -1], float('inf')
        l=0

        for r in range(len(s)):
            c = s[r]
            window[c] = window[c]+1

            if c in countT and window[c] == countT[c]:
                have+=1
            
            while have == need:

                if (r-l+1)<resultLength:
                    result = [l, r]
                    resultLength = r-l+1
                
                #pop from the left of the window
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                
                l+=1
        
        l, r = result
        return s[l: r+1] if resultLength!=float('inf') else ""







