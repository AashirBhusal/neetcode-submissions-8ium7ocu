class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        setNums = set(nums)
        longest = 0

        for i in range(len(nums)):
            if (nums[i] - 1 not in setNums):

                current = nums[i]

                length = 1


                while (current + 1 in setNums):
                    current = current + 1
                    length = length + 1

                if length > longest:
                    longest = length

        return longest






            
            