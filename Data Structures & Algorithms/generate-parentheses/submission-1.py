class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n/2 opening parenthesis, n/2 closing parenthesis
        # put closing parenthesis down if # opening parenthesis < closing parenthesis
        res = []
        curr = []
        
        def generate(opening, closing):
            if opening == closing == n:
                res.append(''.join(curr))
                return
            
            if opening < n:
                curr.append("(")
                generate(opening + 1, closing)
                curr.pop()

            if closing < opening:
                curr.append(")")
                generate(opening, closing + 1)
                curr.pop()
        
        generate(0, 0)
        return res