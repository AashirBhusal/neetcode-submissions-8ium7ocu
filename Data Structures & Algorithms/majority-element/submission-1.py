class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        new_dict = {}

        for s in nums:
            if s not in new_dict:
                new_dict[s] = 0
            
            new_dict[s] += 1

        return max(new_dict, key=new_dict.get)

        

