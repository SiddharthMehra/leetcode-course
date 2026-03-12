class Solution:
    def lexGreaterPermutation(self, S: str, T: str) -> str:

        s = [ord(c) - 97 for c in S]
        t = [ord(c) - 97 for c in T]
        s.sort(reverse = True)
        ans = []

        for i,x in enumerate(t):
            if x in s:
                s.remove(x)
                if s>t[i+1:]:
                    ans.append(x)
                    continue
                
                s.append(x)
                s.sort(reverse = True)
            
            s.sort()
            for y in s:
                if y>x:
                    s.remove(y)
                    ans.append(y)
                    ans.extend(s)
                    break
            break
        
        return "".join(chr(97 + x) for x in ans)
