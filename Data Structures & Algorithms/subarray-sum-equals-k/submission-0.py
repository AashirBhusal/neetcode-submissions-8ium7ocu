class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0]

        i = 0

        total = 0

        while i < len(nums):
            total = total + nums[i]
            prefixSum.append(total)
            i += 1

        seen = {}
        count = 0

        j = 0

        while j < len(prefixSum):
            current = prefixSum[j]
            needed = current - k 

            if needed in seen:
                count = count + seen[needed]

            if current in seen:
                seen[current] += 1
            else:
                seen[current] = 1

            j += 1

        return count



        

        