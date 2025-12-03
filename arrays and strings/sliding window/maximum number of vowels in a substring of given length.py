class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = {'a', 'e', 'i', 'o', 'u'}

        count=0

        for i in range(k):
            count+=int(s[i] in vowels) #first window
        
        ans = count

        for i in range(k, len(s)):
            count+=int(s[i] in vowels) #slide windoe towards right with fixed length k
            count-=int(s[i-k] in vowels)
            ans = max(ans, count)
        
        return ans
        

