#思路都是绕一圈，右下左上循环，计算index；
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)];
        k = 1;
        i = 0;
        while (k <= n * n):
            j = i;
            while (j < n - i):
                result[i][j] = k;
                j += 1;
                k += 1;
            j = i + 1;
            while (j < n - i):
                result[j][n - i - 1] = k;
                j += 1;
                k += 1;
            j = n - i - 2;
            while (j > i):
                result[n - i - 1][j] = k;
                j -= 1;
                k += 1;
            j = n - i - 1;
            while(j > i):
                result[j][i] = k;
                j -= 1;
                k += 1;
            i += 1;
        return result;

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        col=[0,n]
        row=[0,n]

        i,j=0,0
        mat[i][j] = 1

        dir = 'right'
        k=2
        while k <= n*n:
            if dir=='right':
                if j == col[1]-1:
                    dir='down'
                    row[0] +=1
                else:
                    j+=1
                    mat[i][j]=k
                    k+=1
       
                
            elif dir =='down':
                if i == row[1]-1:
                    dir = 'left'
                    col[1] -= 1   
                else:
                    i+=1
                    mat[i][j]=k                
                    k+=1

            
            elif dir == 'left':
                if j == col[0]:
                    dir = 'up'
                    row[1] -=1
                else:
                    j-=1
                    mat[i][j]=k                
                    k+=1


            elif dir == 'up':
                if i == row[0]:
                    dir = 'right'
                    col[0] +=1
                else:
                    i-=1
                    mat[i][j]=k                
                    k+=1
      
        return mat