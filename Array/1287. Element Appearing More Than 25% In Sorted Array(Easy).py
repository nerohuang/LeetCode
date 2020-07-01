class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter
        
        arrCount = Counter(arr);
        lenArr = len(arr);
        for num in arr:
            if arrCount[num] / lenArr > 0.25:
                return num;

##class Solution:
##    def findSpecialInteger(self, arr: List[int]) -> int:
##        n = len(arr) // 4
##        for i in range(len(arr)):
##            if arr[i] == arr[i + n]:
##                return arr[i]