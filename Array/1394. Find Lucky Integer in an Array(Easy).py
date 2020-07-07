class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = [];
        numSet = list(set(arr));
        for num in numSet:
            if num == arr.count(num):
                result.append(num);
        if result == []:
            return -1;
        else:
            return max(result);


##class Solution:
##    def findLucky(self, arr: List[int]) -> int:
##        c = collections.Counter(arr)
##        outputArr = []
##        for i in arr:
##        # Value equals to its frequency.
##            if i == c[i]:
##                outputArr.append(i)
##        if outputArr:
##            return max(outputArr)
##        return -1