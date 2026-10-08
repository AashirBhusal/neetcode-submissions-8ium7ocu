class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)

        left = 1

        for i in range(len(nums)):
            output[i] = left
            left = left * nums[i]

        right = 1

        i = len(nums) - 1

        while i >= 0:
            output[i] = output[i] * right
            right = right * nums[i]
            i = i - 1

        return output

