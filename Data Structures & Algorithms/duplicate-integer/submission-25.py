class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_dict = {}

        for i in nums:
            if i in new_dict:
                return True
            
            else:
                new_dict[i] = True

        return False