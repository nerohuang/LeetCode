class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0;
        while i < len(arr) - 1:
            arr[i] = max(arr[i + 1:]);
            i += 1;
        arr[-1] = -1;
        return arr;

##A = [17,18,5,4,6,1]
##mx = -1;
##for i in range(len(A) - 1, -1, -1):
##    A[i], mx = mx, max(mx, A[i])
##print(A)