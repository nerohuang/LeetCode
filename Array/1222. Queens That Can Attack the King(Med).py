class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        board = [["" for i in range(8)] for j in range(8)];
        for x, y in queens:
            board[x][y] = "*";
        
        kingX = king[0];
        kingY = king[1];
        
        ans = [];
        i = 0
        
        #Up
        while kingY - i >= 0:
            if board[kingX][kingY - i] == "*":
                ans.append([kingX, kingY - i]);
                break;
            else:
                i += 1;
        
        i = 0;
        #Down
        while kingY + i < 8:
            if board[kingX][kingY + i] == "*":
                ans.append([kingX, kingY + i]);
                break;
            else:
                i += 1;
        
        i = 0;
        #Left
        while kingX - i >= 0:
            if board[kingX - i][kingY] == "*":
                ans.append([kingX - i, kingY]);
                break;
            else:
                i += 1;
                
        i = 0;
        #Right
        while kingX + i < 8:
            if board[kingX + i][kingY] == "*":
                ans.append([kingX + i, kingY]);
                break;
            else:
                i += 1;
                
        i = 0;
        j = 0;
        #Left-Up
        while kingX - i >= 0 and kingY - j >= 0:
            if board[kingX - i][kingY - j] == "*":
                ans.append([kingX - i, kingY - j]);
                break;
            else:
                i += 1;
                j += 1;
        
        i = 0;
        j = 0;
        #Right-Up
        while kingX + i < 8 and kingY - j >= 0:
            if board[kingX + i][kingY - j] == "*":
                ans.append([kingX + i, kingY - j]);
                break;
            else:
                i += 1;
                j += 1;
        
        i = 0;
        j = 0;
        #Left-Down
        while kingX - i >= 0 and kingY + j < 8:
            if board[kingX - i][kingY + j] == "*":
                ans.append([kingX - i, kingY + j]);
                break;
            else:
                i += 1;
                j += 1;
        
        
        i = 0;
        j = 0;
        #Rigth-Down
        while kingX + i < 8 and kingY + j < 8:
            if board[kingX + i][kingY + j] == "*":
                ans.append([kingX + i, kingY + j]);
                break;
            else:
                i += 1;
                j += 1;
                
        return ans;

#思路就是从king然后上下左右开始找，只要该方向找到一个就break。

#class Solution:
#    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
#        res = []
#        queens_map = {(i, j) for i,j in queens}
#        for i in [-1, 0, 1]:
#            for j in [-1, 0, 1]:
#                for k in range(1, 8):
#                    x, y = king[0] + i * k, king[1] + j * k
#                    if (x, y) in queens_map:
#                        res.append([x, y])
#                        break
#        
#        return res