class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0:
            return False
        stack = [];
        starStack = [];
        for i, symbol in enumerate(s):
            if symbol == "(":
                stack.append(i);
            if symbol == "*":
                starStack.append(i);
            if symbol == ")":
                if len(stack) > 0:
                    stack.pop();
                elif len(starStack) > 0:
                    starStack.pop();
                else:
                    return False;
        while (len(stack) and len(starStack)):
            if stack.pop() > starStack.pop():
                return False
        return not stack;

# 思路 （括弧：brackets）
# 想法是对的，用stack来存左括号，但问题是现在多了一个*号
# 这个*号能代替（，），还有空格。
# 所以合规格的组合有： “()”,“(*...)”,"(*","*)"
# 所以我们可以用两个stack分别存储左括号和星号的位置
# 当碰到右括号的时候，就先找左括号的stack，如果有，那么就pop
# 出最后一个，如果没有，那么pop出星号stack的最后一个。
# 如果都没有，false
# 当遍历完之后，如果左括号stack还有东西，那么就开始比较
# 怎么样的左括号和*号组合才是合法，那么就是"(*"
# 所以stack的i一对一的要比星号的i小才行
# 只要有一个大了就返回false
# 最后，如果左括号stack还有的话，那就false