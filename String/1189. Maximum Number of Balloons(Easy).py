class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        store = {};
        for character in text:
            store[character] = store.get(character, 0) + 1;
        
        ans = -1;
        noMore = False;

        while not noMore:
            ans += 1;
            for char in "balloon":
                if char not in store:
                    noMore = True;
                else:
                    store[char] -= 1;
                    if store[char] < 0:
                        noMore = True;
        
        return ans;

#class Solution:
#    def maxNumberOfBalloons(self, text: str) -> int:
#        alpha = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
#        for char in text:
#            if char in alpha:
#                alpha[char] += 1
#        return min(alpha['b'], alpha['a'], alpha['l']//2, alpha['o']//2, alpha['n'])
#思路：只要计算B,A,L//2,O//2和N里面最少的那个就行了。