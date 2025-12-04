class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        flat_list = [x for lst in nums for x in lst] # [[3,5,1],[2,3,1]] becomes [3,5,1,2,3,1]

        counts = Counter(flat_list)

        result = [key for key, value in counts.items() if value == len(nums)]

        return sorted(result)
        