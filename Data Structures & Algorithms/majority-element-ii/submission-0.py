class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hashMap = {}

        length = len(nums) / 3

        answer = []


        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1

        for key,value in hashMap.items():
            if value > length:
                answer.append(key)

        return answer


