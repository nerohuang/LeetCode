class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0;
        pairStore = {};
        for pair in dominoes:
            if tuple(sorted(pair)) not in pairStore:
                pairStore[tuple(sorted(pair))] = 1;
            else:
                pairStore[tuple(sorted(pair))] += 1;
        for value in pairStore.values():
            ans += (1 + value - 1) * (value - 1) // 2;
        return ans;

##class Solution:
##    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
##        # step 1: count the dominoes
##        d = collections.defaultdict(int)
##        c = 0
##        for domi in dominoes:
##            p = tuple(sorted(domi))
##            # if p in d:
##                # c += d[p]
##            d[p] += 1
##                
##        # step 2: caculate the pairs. for each pair, number of pairs = n*(n-1)//2
##        # c = 0
##        for n in d.values():
##            s = n*(n-1)//2
##            c += s
##        return c