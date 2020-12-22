class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = [];
        
        def dfs(s, store):
            if not s:
                #这里用store[::]是因为这也可以创建一个新的list
                #存入result而不是直接引用store。
                result.append(store[::]);
                return;
            
            for i in range(1, len(s) + 1):
                prefix, postfix = s[:i], s[i:];
                
                if prefix == prefix[::-1]:
                    store.append(prefix);
                    dfs(postfix, store);
                    store.pop();
        dfs(s, []);
        print(result)

#思路：
#用DFS做：
#一个字符一个字符的切割：分开成为prefix和postfix两个阶段：
#如果prefix是回文，那么储存，然后用postfix递归；
#直到不能再切割，那么当前储存的所有结果就是第i位情况下所有回文的情况
#当然储存返回后，要对store进行pop表明最后一个已经找完。