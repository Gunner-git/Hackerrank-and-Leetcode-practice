class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i in operations:
            if i == "C":
                record.pop()
            elif i == "D":
                record.append(2*(int(record[-1])))
            elif i == "+":
                record.append(int(record[-1])+int(record[-2]))
            else:
                record.append(int(i))

        return sum(record)