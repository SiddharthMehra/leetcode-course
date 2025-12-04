def find_longest_substring(s, k):
    count = defaultdict(int)
    left = ans =0

    for right in range(len(s)):
        count[s[right]]+=1
        while len(count)>k:
            count[left]-=1
            if count[left]==0:
                del count[left]
            
            left+=1
        
        ans = max(ans, right-left+1)
    
    return ans
