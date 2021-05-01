class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lp = 0;
        rp = 2;
        ans = 0;
        while lp < len(s) - 2:
            windows = s[lp: rp + 1];
            if "a" in windows and "b" in windows and "c" in windows:
                ans += len(s) - rp;
                lp += 1;
            else:
                rp += 1;
                if rp == len(s):
                    break;
        return ans

# sliding windows
# 脑瘫了，反向对了，实现没想到。
# 这个首先建立两个pointer， 然后left = 0, right = 2;
# 因为是abc三个字母所以substring至少有3位。
# 然后开始遍历直到left<len(s) - 2；
# 先截出windows=s[lp:rp+1];
# 如果windows里面都含有a,b，c,那么ans += len(s)-rp；
# 因为如果在s[lp. rp + 1]里面有一个符合的，那么
# 在s[lp, len(s) - 1]里面就有len(s) - rp个符合的substring
# 怎么理解呢：比如 abcabc
# 我们在头三个 abc 截出来，会发觉符合，那么其实之后的
# abca， abcab，abcabc也理所当然的符合，因为头三个字符就符合了
# 所以是1+3 = 6-2 = 4, 也就是len(s) - right;
# 然后符合之后left + 1；
# 当不符合的适合right + 1，然后在判断如果rp == len(s)就break；