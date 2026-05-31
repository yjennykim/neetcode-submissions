class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one = ([0] * (len(digits) - 1)) + [1]
        carry = 0
        print("one", one)
        for i in range(len(digits)-1, -1, -1):
            summ = digits[i] + one[i] + carry
            print("sum", summ)
            carry = summ // 10
            digits[i] = summ % 10
        
        if carry > 0:
            return [carry] + digits

        return digits
