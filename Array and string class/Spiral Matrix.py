class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        col = len(matrix)
        row = len(matrix[0])
        col_c = 0
        row_c = 0
        row_show_plus = True
        row_show_neg = False
        col_show_plus = False
        col_show_neg = False
        result = []
        for i in range(col * row):
            result.append(matrix[col_c][row_c])
            
            print(matrix[col_c][row_c])
            matrix[col_c][row_c] = '*'
            if row_show_plus:
                if (row_c + 1 < row) and (matrix[col_c][row_c + 1] != '*'):
                    row_c += 1
                else:
                    row_show_plus = False
                    col_show_plus = True
                    col_c += 1
            elif col_show_plus:
                if (col_c + 1 < col) and (matrix[col_c + 1][row_c] != '*'):
                    col_c += 1
                else:
                    col_show_plus = False
                    row_show_neg = True
                    row_c -= 1
            elif row_show_neg:
                if (row_c - 1 >= 0) and (matrix[col_c][row_c - 1] != '*'):
                    row_c -= 1
                else:
                    row_show_neg = False
                    col_show_neg = True
                    col_c -= 1
            elif col_show_neg:
                if (col_c - 1 >= 0) and (matrix[col_c - 1][row_c] != '*'):
                    col_c -= 1
                else:
                    col_show_neg = False
                    row_show_plus = True
                    row_c += 1
        return result