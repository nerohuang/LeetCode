class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = [];
        newList = [];
        for curList in A:
            revList = curList[::-1];
            for num in revList:
                if num == 0:
                    newList.append(1);
                else:
                    newList.append(0);
            result.append(newList);
            newList = [];
        return result;

##class Solution:
##    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
##        for i in range(len(A)):
##            A[i] = [1-j for j in A[i][::-1]]
##        return A