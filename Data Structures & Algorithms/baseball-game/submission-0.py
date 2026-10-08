class Solution:
    def calPoints(self, operations: List[str]) -> int:
        history = []
        for i,op in enumerate(operations):
            if operations[i] == '+':
                val = history[-1] + history[-2]
                history.append(val)
            elif operations[i] == 'D':
                val = 2 * history[-1]
                history.append(val)
            elif operations[i] == 'C':
                history.pop()
            else:
                history.append(int(operations[i]))
        
        return sum(history)
        