class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def countLive(i, j):
            count = 0;
            if i-1 >= 0 and j-1 >= 0:   count += board[i-1][j-1]%2;
            if i-1 >= 0:                count += board[i-1][j]%2;
            if i-1 >= 0 and j+1 < n:    count += board[i-1][j+1]%2;
            if j-1 >= 0:                count += board[i][j-1]%2;
            if j+1 < n:                 count += board[i][j+1]%2;
            if i+1 < m and j-1 >= 0:    count += board[i+1][j-1]%2;
            if i+1 < m:                 count += board[i+1][j]%2;
            if i+1 < m and j+1 < n:     count += board[i+1][j+1]%2;
            return count;
        
        m,n = len(board), len(board[0]);
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0 or board[i][j] == 2:
                    if countLive(i, j) == 3:
                        board[i][j] = 2;
                else:
                    if countLive(i, j) < 2 or countLive(i, j) > 3:
                        board[i][j] = 3;
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1;
                if board[i][j] == 3: board[i][j] = 0;

#0,2 are "dead", and "dead->live"
#1,3 are "live", and "live->dead"
                    