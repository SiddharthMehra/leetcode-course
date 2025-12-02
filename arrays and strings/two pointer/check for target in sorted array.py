def check_for_target(nums, target):
    left=0
    right = len(nums)-1

    while left<right:
        curr = nums[left]+nums[right]
        if curr == target:
            return True
        if curr<target:
            left+=1
        else:
            right-=1
    
    return False

#Time complexity: O(N)
#space complexity: O(1)
        