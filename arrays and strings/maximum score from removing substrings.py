class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        #ensure "ab" always has higher points than "ba"
        if x<y:
            s = s[::-1]
            x, y = y, x
        
        a_count, b_count, total_points = 0, 0, 0

        for i in range(len(s)):
            if s[i] == "a":
                a_count+=1
            #make "ab" pairs
            elif s[i] == "b":
                if a_count>0:
                    a_count-=1
                    total_points+=x
            #cant form "ab" keep b for future "ba"
                else:
                    b_count+=1
            #non a or b character encountered. calculate points for remaining pairs
            else:
                total_points+=min(b_count, a_count) * y
                a_count, b_count = 0, 0
        
        total_points+=min(b_count, a_count) * y
        return total_points
            

        
