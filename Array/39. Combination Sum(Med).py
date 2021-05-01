class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = [];
        
        def findSum(begin, path, target):
            if not target:
                ans.append(path);
                return;
            
            for i in range(begin, len(candidates)):
                if candidates[i] > target:
                    break;
                
                findSum(i, path+[candidates[i]], target - candidates[i]);
        
        candidates.sort();
        findSum(0, [], target);
        
        return ans;

# 递归
# 先排序，因为可以用相同的，所以就以但前index为下一个递归循环的初始位置
# 然后如果当前数字大于target break就行了。