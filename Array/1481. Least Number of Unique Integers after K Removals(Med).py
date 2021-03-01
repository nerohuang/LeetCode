class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        store = {};
        for num in arr:
            store[num] = store.get(num, 0) + 1;
        
        store = sorted(store.items(), key = lambda x:x[1])
        
        ans = len(store);
        for key, value in store:
            if value <= k:
                k -= value;
                ans -= 1;
            else:
                break;
        
        return ans;