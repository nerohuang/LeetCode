class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0];
        if n == 2:
            return [-1, 1];
        if n % 2 == 1:
            result = [0];
            for i in range(n // 2):
                result.insert(0, -(i + 1));
                result.append(i + 1);
            return result;
        else:
            result = [-1, 1];
            for i in range(1, n // 2):
                result.insert(0, -(i + 1));
                result.append(i + 1);
            return result;

#class Solution:
#    def sumZero(self, n: int) -> List[int]:
#        out = []
#        half = n//2
#        out.extend(range(1, half + 1))
#        out.extend(range(-half, 0))
#        if n%2 == 1:
#            out.append(0)
#        return out