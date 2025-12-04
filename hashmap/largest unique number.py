class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)

        return max((num for num, freq in count.items() if freq==1), default=-1)

        