class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        num = [x + 1 for x in range(m)];
        ans = [];
        
        for query in queries:
            ans.append(num.index(query));
            num.remove(query);
            num.insert(0, query);
        
        return ans;