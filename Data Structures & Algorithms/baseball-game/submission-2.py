class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        ops = []

        for i in range(len(operations)):
            if operations[i] == '+':
                tmp = ops[-1] + ops[-2]
                res += tmp
                ops.append(tmp)
            elif operations[i] == 'C':
                res -= ops.pop()
            elif operations[i] == 'D':
                tmp = ops[-1] * 2
                res += tmp
                ops.append(tmp)
            else:
                res += int(operations[i])
                ops.append(int(operations[i]))
            print(ops)
        
        return res

        