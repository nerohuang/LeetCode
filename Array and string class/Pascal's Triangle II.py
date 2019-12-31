class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex + 1):
            if i < 2:
                result.append(1)
            else:
                for j in range(len(result) - 1):
                    result[j] = result[j] + result[j + 1]
                result.insert(0, 1)
        return result