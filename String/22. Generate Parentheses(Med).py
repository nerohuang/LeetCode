class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans =[];
        def builder(curAns, left, right):
            if len(curAns) == 2 * n:
                ans.append(curAns);
                return;
            #因为只能左括号在前头，所以一开始就写成left<n为第一个判断

            #如果left小于n，那么意思就是可以继续添加左括号，这是每一次递归第一种情况。
            if left < n:
                builder(curAns + "(", left + 1, right);
            #如果左括号比右括号多了，那么可以添加右括号，这是每次递归的第二种情况。
            if right < left:
                builder(curAns + ")", left, right + 1);
        
        builder("", 0, 0);
        
        return ans;

#思路:
#用back track:
#思路其实是因为括号一左一右，而且要保持成对，所以：
#1.每种可能性的长度是2n，当达到2n的时候，那种可能性就完成了。
#2.用left和right记录左括号和右括号的个数。
#3.当left小于n的时候，就可以加左括号，然后进度递归，因为总共就n对括号。
#4.当left大于right的时候，就可以添加右括号，这是一种可能性的分支。
#https://www.youtube.com/watch?v=PCb1Ca_j6OU&ab_channel=basketwangCoding