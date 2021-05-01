class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # check whether can find word, start at (i,j) position 
        def findChar(board, i, j, word):
            if len(word) == 0:# all the characters are checked
                return True;
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
                return False;
            curLoc = board[i][j];# first character is found, check the remaining part
            board[i][j] = '#';# avoid visit agian 
             # check whether can find "word" along one direction
            result = findChar(board, i + 1, j, word[1:]) or findChar(board, i, j + 1, word[1:]) or findChar(board, i - 1, j, word[1:]) or findChar(board, i, j - 1, word[1:]);
            #if cannot find the match charter, deleter # to make it visitalbe again.
            board[i][j] = curLoc;
            return result;
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if findChar(board, i, j, word):
                    return True;
        return False;

# 思路：
# 其实思路类似DFS，但这东西不是树而已
# 因为他寻找轨迹是可以上下左右四方向行走，所以为了防止走重复的
# 走过的地方要标记。当该路线寻找完改回来就行了
