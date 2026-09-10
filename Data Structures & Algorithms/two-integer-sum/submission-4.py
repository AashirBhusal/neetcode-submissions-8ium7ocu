class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}

        for i in range(len(nums)):
            if target - nums[i] in new_dict:
                return [new_dict[target - nums[i]], i]
            else:
                new_dict[nums[i]] = i