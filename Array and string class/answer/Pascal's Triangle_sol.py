class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return ([])
        if numRows == 1:
            return ([[1]])
        if numRows == 2:
            return ([[1], [1, 1]])
        small = self.generate((numRows-1))
        if small != None:
            last = small[-1]
        new = [1]
        for i in range(len(last)-1):
            new.append(last[i]+last[i+1])
        new.append(1)
        small.append(new)
        return small