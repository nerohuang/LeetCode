class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        x = len(M);
        y = len(M[0]);
        result = [[0] * y for i in range(x)];
        curSum = 0;
        for i in range(x):
            for j in range(y):
                count = 1;
                curSum = M[i][j];
                if i - 1 >= 0:
                    curSum += M[i - 1][j];
                    count += 1;
                if i + 1 <= x - 1:
                    curSum += M[i + 1][j];
                    count += 1;
                if j - 1 >= 0:
                    curSum += M[i][j - 1];
                    count += 1;
                if j + 1 <= y - 1:
                    curSum += M[i][j + 1];
                    count += 1;
                if i - 1 >= 0 and j - 1 >= 0:
                    curSum += M[i - 1][j - 1];
                    count += 1;
                if i - 1 >= 0 and j + 1 <= y - 1:
                    curSum += M[i - 1][j + 1];
                    count += 1;
                if i + 1 <= x - 1 and j - 1 >= 0:
                    curSum += M[i + 1][j - 1];
                    count += 1;
                if i + 1 <= x - 1 and j + 1 <= y - 1:
                    curSum += M[i + 1][j + 1];
                    count += 1;
                result[i][j] = curSum // count;
        return result;

#class Solution:
#    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
#        w, h = len(M[0]), len(M)
#        result = []
#        M_temp = []
#        for i in range(h):
#            row_left = M[i] + [0, 0]
#            row_center = [0] + M[i] + [0]
#            row_right = [0, 0] + M[i]
#            temp = [l+c+r for l, c, r in zip(row_left, row_center, row_right)]
#            M_temp.append(temp)
#
#        row_up = [0] * (w+2)
#        for i in range(h-1):
#            row_cur = M_temp[i]
#            row_down = M_temp[i+1]
#            temp = [u+c+d for u, c, d in zip(row_up, row_cur, row_down)]
#            result.append(temp)
#            row_up = row_cur
#        row_cur = M_temp[-1]
#        temp = [u+c for u, c in zip(row_up, row_cur)]
#        result.append(temp)
#
#
#        out = []
#        if h > 1:
#            if w > 1:
#                d1 = [4] + [6]*(w-2) + [4]
#                d2 = [6] + [9]*(w-2) + [6]                
#                out.append([int(x/y) for x, y, in zip(result[0][1:-1], d1)])
#                for i in range(h-2):
#                    out.append([int(x/y) for x, y, in zip(result[i+1][1:-1], d2)])
#                out.append([int(x/y) for x, y, in zip(result[-1][1:-1], d1)])
#            else:
#                d1 = [2] + [3]*(h-2) + [2]
#                for i in range(h):
#                    out.append([int(result[i][0]/d1[i])])
#
#        else:
#            if w > 1:
#                d1 = [2] + [3]*(w-2) + [2]
#                out.append([int(x/y) for x, y, in zip(result[-1][1:-1], d1)])
#            else:
#                out = M
#
#
#        return out