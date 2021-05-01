class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort();
        ans = [];
        
        def findSum(begin, path, target):
            if not target:
                ans.append(path);
                return;
            
            for i in range(begin, len(candidates)):

                #=====================1===============
                if i > begin and candidates[i] == candidates[i - 1]:
                    continue;
                #=====================1===============
                
                if candidates[i] > target:
                    break;
            
                findSum(i + 1, path + [candidates[i]], target - candidates[i]);
                
        findSum(0, [], target);
        return ans;

##思路
# 递归，和前面一题一样不过有一个特别要注意的点
# 就是可能会有重复。
# 如果递归前一个和后一个相同的话要continue跳过
# 因为如果是一样的话，那么这个相同数字的可能组合
# 在前面一个已经找过一遍了， 所以后一个就不要再找一遍
# 浪费时间了。