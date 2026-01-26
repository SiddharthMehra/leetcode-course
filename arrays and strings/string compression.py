class Solution:
    def compress(self, chars: List[str]) -> int:
        ans, i = 0, 0

        while i<len(chars):
            letter = chars[i]
            count = 0

            while i<len(chars) and chars[i] == letter:
                count+=1
                i+=1
            
            #place letters and increment counter for the count
            chars[ans] = letter
            ans+=1

            #place count after the letter
            
            if count>1:
                for c in str(count):
                    chars[ans] = c
                    ans+=1
            
        return ans
