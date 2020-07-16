class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def combinationSum(nums, begin, target, path, result):
            if target == 0:
                result.append(path);
                return;
            for i in range(begin, len(nums)):
                if nums[i] > target:
                    break;
                combinationSum(nums, i + 1, target - nums[i], path + [nums[i]], result);
                
        nums = [i for i in range(1, 10)];
        result = [];
        combinationSum(nums, 0, n, [], result);
        finalResult = []
        for ans in result:
            if len(ans) == k:
                finalResult.append(ans);
        return(finalResult);

#class Solution:
#    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
#        def combinationSum3Helper(offset, total, used, partial):
#            if total == n and used == k:
#                result.append(list(partial))
#                return
#            if offset > 9 or total > n or used > k:
#                return
#            
#            for i in range(offset, 10):
#                combinationSum3Helper(i + 1, total + i, used + 1, partial + [i])
#        
#        result = []
#        combinationSum3Helper(1, 0, 0, [])
#        return result