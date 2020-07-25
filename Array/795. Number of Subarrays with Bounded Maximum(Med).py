class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        store = [];
        for i in range(len(A)):
            curStore = [];
            j = i;
            while j < len(A) and A[j] <= R:
                curStore.append(A[j]);
                if max(curStore) >= L:
                    newStore = curStore.copy();
                    store.append(newStore);
                j += 1;
        return(len(store)); 


#class Solution:
#    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
#        res = i = count = 0
#        for j, n in enumerate(A):
#            if L <= n <= R:
#                count = j - i + 1
#                res += count
#            elif n > R:
#                i = j + 1
#                count = 0
#            else:
#                res += count
#        return res