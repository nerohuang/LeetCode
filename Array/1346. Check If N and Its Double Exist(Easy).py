class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        while len(arr) != 0:
            curNum = arr[0];
            arr.pop(0);
            if curNum * 2 in arr or curNum / 2 in arr:
                return True;
        return False;

#class Solution:
#    def checkIfExist(self, arr: List[int]) -> bool:
#        d={}
#        for i in range(len(arr)):
#            if arr[i]*2 in d or (arr[i]%2==0 and arr[i]//2 in d):# need to check if arr[i]%2==0 as 7//2 returns 3
#                return True
#            else:
#                d[arr[i]]=1
#        return False