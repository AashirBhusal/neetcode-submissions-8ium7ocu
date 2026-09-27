class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        new_dict = {}

        for i in nums:
            if i not in new_dict:
                new_dict[i] = 0
            new_dict[i] += 1

        for j in new_dict:
            if new_dict[j] > len(nums) // 2:
                return j

            
