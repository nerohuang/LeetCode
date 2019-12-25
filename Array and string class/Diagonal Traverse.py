class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        m_col = len(matrix)
        m_row = len(matrix[0])
        col_c = 0
        row_c = 0
        m_size = m_col * m_row
        m_sort = []
        result = []
        sort_list = []
        
        if m_col > m_row :
            m_min = m_row
        else:
            m_min = m_col
            
        if m_size == 1:
            m_sort.append(matrix[0][0])
            return(m_sort)
        if m_size == 2:
            if m_col > m_row:
                m_sort.append(matrix[0][0])
                m_sort.append(matrix[1][0])
            else:
                m_sort.append(matrix[0][0])
                m_sort.append(matrix[0][1])
            return(m_sort)
        
        sort_list = [1, 1]
        count = 1
        m_size = m_size - 2
        while m_size >0:
            if count + 1 <= m_min:
                count = count + 1
            if m_size - 2*count >= 0:
                sort_list.insert(int(len(sort_list)/2),count)
                sort_list.insert(int(len(sort_list)/2),count)
                m_size = m_size - 2*count
            else:
                sort_list.insert(int(len(sort_list)/2),m_size)
                m_size = 0
        print(sort_list)
        for i in range(len(sort_list)):
            if ((i + 1) % 2 == 1):
                for l in range(sort_list[i]):
                    
                    print(sort_list[i], l, col_c, row_c)
                    result.append(matrix[col_c][row_c])
                    if (col_c - 1 >= 0) and (row_c + 1 < m_row):
                        col_c = col_c - 1
                        row_c = row_c + 1
                if row_c + 1 < m_row:
                    row_c = row_c + 1
                else:
                    col_c = col_c + 1
            else:
                for l in range(sort_list[i]):
                    print(sort_list[i], l, col_c, row_c)
                    result.append(matrix[col_c][row_c])
                    if row_c - 1 >= 0 and (col_c + 1 < m_col):
                        col_c = col_c + 1
                        row_c = row_c - 1
                if col_c + 1 < m_col:
                    print(col_c)
                    col_c = col_c + 1
                else:
                    row_c = row_c + 1
        return result