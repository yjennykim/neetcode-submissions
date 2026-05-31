class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        numbers = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "*": "",
            "0": "+",
        }

        def recurse(curr, index):
            if index == len(digits):
                res.append(curr)
                return
            
            options = numbers[digits[index]]
            for letter in options:
                recurse(curr + letter, index + 1)
        
        if len(digits) == 0:
            return []

        recurse("", 0)

        return res
