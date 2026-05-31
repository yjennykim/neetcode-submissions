from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collect = defaultdict(list)

        # Sort each string, have that as the key to a hashmap
        for st in strs:
            sorted_key = ''.join(sorted(st))
            collect[sorted_key].append(st)

        # Return only the values 
        return list(collect.values())