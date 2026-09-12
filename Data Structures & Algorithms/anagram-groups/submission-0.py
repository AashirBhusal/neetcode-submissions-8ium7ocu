class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list = {}

        for s in strs:
            key = "".join(sorted(s))
            
            if key not in new_list:
                new_list[key] = []

            new_list[key].append(s)

        return list(new_list.values())

        

            

            
