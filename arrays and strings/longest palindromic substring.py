class Solution:
    def longestPalindrome(self, s:str)->str:
        if not s:
            return ""
        
        start = end = 0
        #expand around centre
        def expand(left, right):
            nonlocal start, end
            while left>=0 and right<len(s) and s[left] == s[right]:
                #check if current number of elements are greater than length of the current largest palindrome
                if right - left > end - start:
                    start, end = left, right
                #expanding around centre
                left-=1
                right+=1
        
        for i in range(len(s)):
            expand(i, i) # for odd length palindrome with a definitive central element
            expand(i, i+1) # for even length palindromes
        
        return s[start:end+1]
    



