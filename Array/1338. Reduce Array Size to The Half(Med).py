class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        arrLen = len(arr);
        arr.sort();
        numStore = {};
        for num in arr:
            numStore[num] = numStore.get(num, 0) + 1;
        
        ans = 0;
        count = 0;
        
        #这个是有关dictionary里面根据item排序，从大到小；
        for x in sorted(numStore.items(), key = lambda x : -x[1]):
            count += x[1];
            ans += 1;
            if count >= arrLen/2:
                return ans;