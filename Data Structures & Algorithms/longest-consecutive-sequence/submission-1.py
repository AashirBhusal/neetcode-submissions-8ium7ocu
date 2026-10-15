class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)

        longest = 0 

        for i in nums:
            if i - 1 not in setNums:
                current = i 

                length = 1

                while current + 1 in setNums:
                    current += 1
                    length += 1

                if length > longest:
                    longest = length 

        return longest