class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort();
        for i in range(len(arr) - 2):
            if arr[i + 1] - arr[i] != arr[i + 2] - arr[i + 1]:
                return False;
        return True;

#class Solution:
#    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
#        minarr = 10**6
#        maxarr = -10**6
#        s = set(arr)
#        for e in arr:
#            if e < minarr:
#                minarr = e
#            if e > maxarr:
#                maxarr = e
#        diff = (maxarr - minarr) // (len(arr) - 1)
#        if diff == 0:
#            return True
#        if len(s) != len(arr):
#            return False
#        for i in range(1, len(arr)):
#            if minarr + i*diff not in s:
#                return False
#        return True