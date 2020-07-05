class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        import numpy as np;
        ans = 0;
        martix = np.array([[0 for x in range(m)] for y in range(n)]);
        for x, y in indices:
            martix[x] = [num + 1 for num in martix[x]];
            martix[:, y] = [num + 1 for num in martix[:, y]];
        for col in martix:
            for num in col:
                if num % 2 == 1:
                    ans += 1;
        return ans;

#class Solution:
#    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
#        odd_rows, odd_cols = [False] * n, [False] * m
#        for r, c in indices:
#            odd_rows[r] ^= True
#            odd_cols[c] ^= True
#        return sum(ro ^ cl for ro in odd_rows for cl in odd_cols)