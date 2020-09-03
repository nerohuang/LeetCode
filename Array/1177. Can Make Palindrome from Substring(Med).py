#class Solution:
#    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
#        ans = []
#        oddCount = 0;
#        char = {};
#        for left, right, k in queries:
#            for charter in s[left:right + 1]:
#                if charter in char:
#                    char[charter] += 1;
#                else:
#                    char[charter] = 1;
#            for charter in char:
#                if char[charter] % 2 == 1:
#                    oddCount += 1;
#            if len(char) == 1 or int(oddCount / 2) <= k:
#                ans.append(True);
#            else:
#                ans.append(False);
#            char = {}
#            oddCount = 0;
#        return ans;
#

#题思路：对于给定一个query = [left,right,k]，很容易能求出这个区间内每个字符出现的次数，
#如果某个字符出现了偶数次，那说明不需要经过任何改变，这个字符就能组成回文。所以这里只需要
#计算有多少个字符出现的次数是奇数，假设有x个字符出现的次数为奇数，那么至少就需要经过x/2次改变，
#才能形成回文。这里有一种情况例外，那就是只有一个字符出现的次数为奇数，那么可以不需要做任何改变。






s = 'abcda'
queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
grid = [[0] * len(s) for _ in range(26)]
count = [0] * 26
for i,v in enumerate(s):
    for j in range(26):
        grid[j][i] = grid[j][i-1]
    inx = ord(v) - ord('a')
    count[inx] += 1
    grid[inx][i] = count[inx]
res = []
for left,right,k in queries:
    diff = 0
    for i in range(26):
        if left > 0 and (grid[i][right] - grid[i][left-1]) % 2 != 0:
            diff += 1
        elif left == 0 and grid[i][right] % 2 != 0:
            diff += 1
    if diff == 1 or diff / 2 <= k:
        res.append(True)
    else:
        res.append(False)