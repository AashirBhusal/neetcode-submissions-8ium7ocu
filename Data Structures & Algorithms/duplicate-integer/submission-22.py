class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}

        for i in nums:
            if i in numsDict:
                return True

            else:
                numsDict[i] = 1

        return False

