class Solution(object):
    def reorderedPowerOf2(self, N):
        #calculate counter of N and check if the counter matches with any power of 2 
        # 1<<b is literally 2^b
        count = Counter(str(N))
        return any(count == Counter(str(1<<b)) for b in range(31))
