class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        inArr = []
        notInArr = []
        result = [];
        arrDict = {num : 0 for num in arr2};
        for num in arr1:
            if num in arrDict:
                arrDict[num] += 1;
            else:
                notInArr.append(num);
        notInArr.sort();
        for num in arr2:
            for i in range(arrDict[num]):
                result.append(num);
        return result + notInArr;

##class Solution:
##    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
##        result = []
##        counter = collections.Counter(arr1)
##        
##        for num in arr2:
##            if num in counter:
##                result.extend([num] * counter[num])                
##                del counter[num]
##        other = []
##        for num, freq in counter.items():
##            other.extend([num] * freq)
##        return result + sorted(other)