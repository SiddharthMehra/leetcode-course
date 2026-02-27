class Solution:
    def sortVowels(self, s: str) -> str:

        vowel_set = set("aeiouAEIOU")
        vowels = [ c for c in s if c in vowel_set]
        vowels.sort()

        result = []
        it = iter(vowels)

        for c in s:
            result.append(next(it) if c in vowel_set else c)
        
        return ''.join(result)

        
