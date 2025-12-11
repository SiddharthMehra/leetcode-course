class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        attempts = len(nums)-k
        stack = []
        for num in nums:
            while stack and num<stack[-1] and attempts>0: #try for lowest element at the start 
                stack.pop()
                attempts-=1
            stack.append(num)
        
        return stack[:k]