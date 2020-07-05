#没做出来

##class Solution:
##    def tictactoe(self, moves: List[List[int]]) -> str:
##        A=[0]*8
##        B=[0]*8
##        for i in range(len(moves)):
##            r,c=moves[i]
##            player = A if i%2==0 else B
##            player[r] += 1
##            player[c+3] += 1
##            if r==c:
##                player[6] += 1
##            if r==2-c:
##                player[7] += 1
##        for i in range(8):
##            if A[i]==3:
##                return "A"
##            if B[i]==3:
##                return "B"
##        
##        return "Draw" if len(moves) == 9 else "Pending"

# 
#          0    1    2  cols
#     0   [ ]  [ ]  [ ]
#     1   [ ]  [ ]  [ ]
#     2   [ ]  [ ]  [ ]
#   rows
# 
# 0. row 0  --> player[r]
# 1. row 1  --> player[r] 
# 2. row 2  --> player[r]
# 3. col 0  --> player[c+3] (+3 to shift to 'cols' area)
# 4. col 1  --> player[c+3]
# 5. col 2  --> player[c+3]
# 6. diagonal top left - bottom right  --> player[6]     r==c:   {0,0}, {1,1}, {2,2}
# 7. diagonal top right - bottom left  --> player[7]     r==2-c: {2,0}, {1,1}, {0,2}