class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)
        listNums = list(setNums)

        if sorted(listNums) == sorted(nums):
            return False
        else:
            return True