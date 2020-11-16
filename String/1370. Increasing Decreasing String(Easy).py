class Solution:
    def sortString(self, s: str) -> str:
        store = {};
        alpha = set();
        for c in s:
            store[c] = store.get(c, 0) + 1;
            alpha.add(c);
        alphaSort = list(alpha);
        alphaSort.sort()
        ans = "";
        i = 0;
        j = 0;
        while i < len(s):
            for c in alphaSort:
                if store[c] > 0:
                    ans += c;
                    store[c] -= 1;
                    i += 1;
            for c in reversed(alphaSort):
                if store[c] > 0:
                    ans += c;
                    store[c] -= 1;
                    i += 1;
        
        return ans;