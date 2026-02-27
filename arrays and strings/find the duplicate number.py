class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #floyd hare and tortoise
        tortoise = hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        #find entrance to the cycle
        tortoise = nums[0]
        while tortoise!=hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
        
