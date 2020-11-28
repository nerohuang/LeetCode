class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or len(set(list(s))) == 1 or s == s[::-1]:
            return s
        
        def search(s, i, j):
            store = ""
            while (i >= 0 and j < len(s) and s[i] == s[j]):
                if i == j:
                    store = s[i];
                else:
                    store = s[i] + store + s[j];
                i -= 1;
                j += 1;
            return store
        
        ans = "";
        for i in range(1, len(s)):
            store1 = search(s, i, i);
            store2 = search(s, i - 1, i);
            longStore = store1 if len(store1) > len(store2) else store2;
            ans = longStore if len(longStore) > len(ans) else ans;
            
        return ans

#思路：
#假设两种可能性：
#s[i] == s[i - 1] 和 s[i] != s[i - 1]
#第一种意思是以一个数为中心然后两边对称，第二种是以两个相同的数为中心然后堆成。
#其实不用先判断是否相等，都先塞进去函数search里面进行扩展比较就行了。
#在函数里面设置一下条件：
#如果塞进去i 和 j其实是一个位置的那么就是第一种情况下扩展
#如果塞进去i 和 j不是一个位置那么以第二种情况下扩展
#扩展用two pointer进行一增一减扩展
#然后比较两个情况下返回的结果，选最大的那个再和答案比较。