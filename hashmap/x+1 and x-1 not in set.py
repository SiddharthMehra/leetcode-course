def find_numbers(nums):
    ans=[]
    num_set = set(nums)

    for num in num_set:
        if (num-1) not in num_set and (num+1) not in num_set:
            ans.append(num)
    
    return ans