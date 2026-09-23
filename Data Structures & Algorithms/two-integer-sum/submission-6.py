class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}

        for i in range(len(nums)):
            diff = target - nums[i]

           

            if diff in new_dict:
                return [new_dict[diff],i]

            new_dict[nums[i]] = i

            