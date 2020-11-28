class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = [];
        ans = 0;
        for c in s:
            if c not in store:
                store.append(c);
                ans = max(ans, len(store));
            else:
                ans = max(ans, len(store));
                store.append(c);
                i = store.index(c);
                store = store[i + 1:]
        
        return ans