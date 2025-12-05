class Solution:
    def customSortString(self, order: str, s: str) -> str:
        string_freq = Counter(s)
        ans = []

        for char in order:
            if char in string_freq:
                ans.append(char * string_freq[char])

                del string_freq[char]
        
        for unordered_element in string_freq:
            ans.append(unordered_element * string_freq[unordered_element])
        
        return ''.join(ans)