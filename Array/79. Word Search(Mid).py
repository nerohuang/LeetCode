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

#class Solution:
#    def exist(self, b, w):
#        if not b or not b[0]: return False
#        bc = Counter(chain(*b))
#        wc = Counter(w)
#        if any(c > bc[s] for s, c in wc.items()): return False
#        m, n, wl = len(b), len(b[0]), len(w) - 1
#        def dfs(d: int, x: int, y: int) -> bool:
#            if w[d] != b[y][x]: return False
#            if d == wl: return True
#            c, b[y][x] = b[y][x], ''
#            if x > 0 and dfs(d + 1, x - 1, y): return True
#            if x < n-1 and dfs(d + 1, x + 1, y): return True
#            if y > 0 and dfs(d + 1, x, y - 1): return True
#            if y < m-1 and dfs(d + 1, x, y + 1): return True
#            b[y][x] = c
#            return False
#        return any(dfs(0, j, i) for i in range(m) for j in range(n) if w[0] == b[i][j])