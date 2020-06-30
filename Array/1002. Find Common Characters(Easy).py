class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = [];
        chars = []
        count = 0;
        for char in A[0]:
            chars.append(char);
        for char in chars:
            for i in range(1, len(A)):
                if char in A[i]:
                    A[i] = A[i].replace(char, '', 1);
                    count += 1;
            if count == len(A) - 1:
                result.append(char);
            count = 0;
        return result;

##class Solution:
##    def commonChars(self, A: List[str]) -> List[str]:
##        answer = []
##        sorted(A)
##        for i,val in enumerate(A[0]):
##            if all(val in string for string in A[1:]):
##                for i in range(1,len(A)):
##                    A[i] = A[i].replace(val,'',1)
##                answer.append(val)
##        return answer