class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsTuple = dict.fromkeys(nums)
        if len(numsTuple) != len(nums):
            return True
        else:
            return False