class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def countp(row):
            ans = 0;
            if "p" in row[rookLoc[1]:]:
                if "B" not in row[rookLoc[1]:row[rookLoc[1]:].index("p") + rookLoc[1]]:
                    ans += 1;
            if "p" in row[:rookLoc[1]]:
                if "B" not in row[:rookLoc[1]]:
                    ans += 1;
                elif "p" in row[row[:rookLoc[1]].index("B"):rookLoc[1]]:
                    print(row[row[:rookLoc[1]].index("B"):rookLoc[1]])
                    ans += 1;
            return ans;
        
        
        rookLoc = [];
        ans = 0;
        for i, row in enumerate(board):
            if "R" in row:
                rookLoc.append(i);
                rookLoc.append(row.index("R"));
        row = board[rookLoc[0]];
        ans += countp(row);
        col = []
        for i in range(8):
            col.append(board[i][rookLoc[1]]);
        ans += countp(col);
        return ans;

##class Solution:
##    def numRookCaptures(self, board: List[List[str]]) -> int:
##        def check(indices):
##            for i, j in indices:
##                if board[i][j] == '.':
##                    continue
##                if board[i][j] == 'B':
##                    return 0
##                if board[i][j] == 'p':
##                    return 1
##            return 0
##        
##        for i in range(len(board)):
##            for j in range(len(board[i])):
##                if board[i][j] == 'R':
##                    return sum([
##                        check(((i, j) for j in range(j+1, len(board[i])))),
##                        check(((i, j) for i in range(i+1, len(board)))),
##                        check(((i, j) for j in range(j-1, -1, -1))),
##                        check(((i, j) for i in range(i-1, -1, -1))),
##                    ])
##        return 0