class Solution:
    def thousandSeparator(self, n: int) -> str:
        storeOne = "";
        storeTwo = [];
        nStr = str(n);
        for i in range(len(nStr) - 1, -1, -1):
            if len(storeOne) != 3:
                storeOne += nStr[i]
            else:
                storeTwo.append(storeOne[::-1]);
                storeOne = ""
                storeOne += nStr[i];
        if storeOne:
            storeTwo.append(storeOne[::-1]);
        if storeTwo == []:
            return nStr
        return ".".join(storeTwo[::-1])