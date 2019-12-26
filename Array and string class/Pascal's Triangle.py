class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0:
            return result
        for i in range(numRows):
            row = []
            print(i)
            if i < 2:
                for l in range(i + 1):
                    row.append(1)
                result.append(row)
            else:
                middle = []
                for l in range(len(result[i - 1]) - 1):
                    middle.append(result[i-1][l] + result[i-1][l + 1])
                row = [1] + middle + [1]
                print(row)
                result.append(row)
        return result