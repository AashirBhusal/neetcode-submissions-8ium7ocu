class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dictnums = {}

        for i in nums:
            if i in dictnums:
                return True
            else:
                 dictnums[i] = True

        
        return False
      
        