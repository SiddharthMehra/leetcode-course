class Solution:
    def robotWithString(self, s: str) -> str:
        cnt, t, p = Counter(s), [], []

        for ch in s:
            t.append(ch)
            cnt[ch]-=1
            if cnt[ch]==0:
                del cnt[ch]

            while cnt and t and min(cnt.keys())>=t[-1]: # check if there exists any smaller element in s than t
                p.append(t.pop())
        
        p.extend(reversed(t))  # insert rest t elements in p
        return ''.join(p)
