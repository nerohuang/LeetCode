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

#class Solution:
#    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#        c = collections.Counter(arr1)
#        res = []       
#        for i in arr2:
#            res += [i]*c.pop(i)  
#        return res + sorted(c.elements())