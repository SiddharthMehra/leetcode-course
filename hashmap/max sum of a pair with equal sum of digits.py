class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = float('-inf')
        hashmap = defaultdict(int)

        for num in nums:
            current = 0
            n = num

            while n:
                current+=n%10
                n//=10
            if current in hashmap:
            
                ans = max(ans, num + hashmap[current])

            hashmap[current] = max(hashmap[current], num)
        
        return ans if ans!=float('-inf') else -1


