class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortArr = sorted(list(set(arr)));
        result = [];
        dictNum = {};
        i = 1;
        for num in sortArr:
            dictNum[num] = i;
            i += 1;
        for num in arr:
            result.append(dictNum[num]);
        return result;

##class Solution:
##    def arrayRankTransform(self, nums: List[int]) -> List[int]:
##        ranks = {num: i for i, num in enumerate(sorted(list(set(nums))), start=1)}
##        return [ranks[x] for x in nums]