class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0;
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i + 1, 0);
                arr.pop();
                i += 1;
            i +=1;

##class Solution:
##    def duplicateZeros(self, arr: List[int]) -> None:
##        """
##        Do not return anything, modify arr in-place instead.
##        """
##        from collections import deque
##        
##        seen = deque()
##        
##        for n in arr:
##            seen.append(n)
##        
##        curr = 0
##        
##        while curr < len(arr):
##            item = seen.popleft()
##            arr[curr] = item
##            
##            if item == 0 and curr != len(arr) - 1:
##                arr[curr + 1] = item
##                curr += 1
##            
##            curr += 1