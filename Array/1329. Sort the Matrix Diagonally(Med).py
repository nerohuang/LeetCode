class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        store = [];
        ans = []
        m = len(mat);
        n = len(mat[0]);
        insert = False
        for i in range(n):
            store.append([mat[0][i]])
        for i in range(1, m):
            for j in range(n):
                if not insert:
                    store.insert(0, [mat[i][j]]);
                    insert = True;
                else:
                    store[j].append(mat[i][j]);
            insert = False;
        
        for i in range(len(store)):
            store[i].sort();
        
        print(store)
        count = 0;
        newStore = [];
        i = 0;
        while store:
            if count < n - 1:
                newStore.append(store[i].pop())
                if store[i] == []:
                    del store[i]
                else:
                    i += 1;
                count += 1;
            else:
                newStore.append(store[i].pop());
                if store[i] == []:
                    del store[i]
                ans.insert(0, newStore);
                newStore = [];
                i = 0;
                count = 0;
        return (ans)


#class Solution:
#    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
#        row = len(mat)
#        col = len(mat[0])
#        for i in range(row-1):
#            vals = sorted([mat[i+k][k] for k in range(min(row-i, col))])
#            for k in range(min(row-i, col)):
#                mat[i+k][k] = vals[k]
#        for j in list(range(col-1))[1:]:
#            vals = sorted([mat[k][j+k] for k in range(min(row, col-j))])
#            for k in range(min(row, col-j)):
#                mat[k][j+k] = vals[k]
#        return mat