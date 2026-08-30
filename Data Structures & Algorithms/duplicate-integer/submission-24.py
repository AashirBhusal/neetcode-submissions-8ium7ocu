class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       dictnums = {}

       for i in nums:
        if i in dictnums:
            return True
        else:
            dictnums[i] = 1

       return False