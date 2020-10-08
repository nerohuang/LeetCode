/**
 * @param {string} s
 * @return {number}
 */
var countBinarySubstrings = function(s) {
    ans = 0;
    pre = 0;
    cur = 1;
    
    for (let i = 1; i < s.length; i++){
        if (s[i - 1] != s[i]){
            ans += Math.min(pre, cur);
            pre = cur;
            cur = 1;
        }
        else{
            cur += 1;
        }
    }
    
    return ans + Math.min(pre, cur);
};

/*
思路：就是就是对称找
先是计算前面n个相同的数字，然后当发觉当前数字和上一个数字不一样的时候，就可以找到对称里面
最小数量的那个然后累加进去答案
00000 1111
  000 111
   00 11
    0 1
这里有4个，而1累计4个，所以取最小的
*/