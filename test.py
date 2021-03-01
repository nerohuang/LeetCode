candidates = [2,5,2,1,2]
target = 5

        ans = [];
        candidates.sort();

        def findSum(store, i, target):
            if not target:
                if store not in ans:
                    ans.append(store);
                return

            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue;
                if target >= candidates[j]:
                    findSum(store + [candidates[j]], j + 1, target - candidates[j]);
                else:
                    break;
            return

        findSum([], -1, target);
print(ans)