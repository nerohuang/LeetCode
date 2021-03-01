class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0;
        for dis in left:
            ans = max(ans, dis);
        for dis in right:
            ans = max(ans, n - dis);
        return ans

#思路：
#要注意一个点，就是碰到转头的话其实并不影响
#他到底要走多远，他该走多远还是走多远。。
#所以这就好理解了
#朝左的最大就是左边最远的 max(left)
#朝右最小的就是最远的 n - mix(right)