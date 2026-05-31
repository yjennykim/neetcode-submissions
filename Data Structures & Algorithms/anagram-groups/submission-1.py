class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted value : []
        """
            {sorted value : [original input strings]}
        """
        table = {}
        for s in strs:
            sortedStr = ''.join(sorted(s)) # sorted() outputs a list
            if sortedStr not in table:
                table[sortedStr] = []
            table[sortedStr].append(s)
        
        return table.values() # values() outputs a list 

            