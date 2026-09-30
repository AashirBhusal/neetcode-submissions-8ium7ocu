class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = {}

        for i in nums:
            if i not in new_dict:
                new_dict[i] = 0
            new_dict[i] += 1


        bucket = [[] for i in range(len(nums) + 1)]

        for i in new_dict:
            bucket[new_dict[i]].append(i)

        result = []

        freq = len(nums)

        for i in reversed(bucket):
            result += i
            if len(result) == k:
                break
        
        return result
        # while freq > 0:
           
        #    ##[[], [], [3],[]]

        #     for i in bucket:
        #         result.append(bucket[freq])
            
        #     if len(result) == k:
        #         return result
            
        #     freq -= 1
        print(result)
