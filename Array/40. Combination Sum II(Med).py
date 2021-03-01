class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = [];
        candidates.sort();

        def findSum(store, i, target):
            if not target:
                if store not in ans:
                    ans.append(store);
                return

            
            for j in range(i, len(candidates)):
                #这一段很关键
                #=====================
                if j > i and candidates[j] == candidates[j - 1]:
                    continue;
                #========================
                if target >= candidates[j]:
                    findSum(store + [candidates[j]], j + 1, target - candidates[j]);
                else:
                    break;
            return
        
        findSum([], 0, target);
        return ans

##思路
# 正常递归思路，其实能想出来
# 有两点要注意很重要：
# 1. 不要用append，用append的话记得要pop
# 2. 要加上 很关键这一段，这一段就是为了防止
#    超时的。他的作用就是如果一前一后的数字
#    是相同的，那么前一个里面成立的所有选项
#    在后一个里面都不会成立或者已经成立过了。
#    思考一下：
#    candidates = [1,1,2,5,6,7,10], target = 8
#    如果已经找到[1,1,6] [1, 7]
#    那么为了防止重复，第二个1就应该直接过掉。因为
#    第一个1已经把可能性找完了。