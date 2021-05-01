class Solution:
    def calculate(self, s: str) -> int:
        stack = [];
        operators = {'+', '-', '*', '/'};
        tmp = 0;
        sign = '+'
        for i in range(len(s)):
            if s[i] not in operators and s[i] != ' ':
                tmp = tmp*10 + int(s[i]);
            if s[i] in operators or i == len(s) - 1:
                if sign == '+':
                    stack.append(tmp);
                if sign == '-':
                    stack.append(-tmp);
                if sign == '*':
                    tmp = tmp * stack.pop();
                    stack.append(tmp);
                if sign == '/':
                    num = stack.pop();
                    if num > 0:
                        stack.append(num//tmp);
                    else:
                        stack.append(-((-num)//tmp));
                sign = s[i];
                tmp = 0;
        return sum(stack)

# 思路：
# 基础想法是对的，没转过来
# 其实就是把所有结果扔进去一个stack里面最后sum
# 开始遍历整个string
# 如果遇到连续的数字，那么就用tmp = tmp*10 + int(s[i]);
# 进行记录。
# 当遇到是计算符号是，那么对上一个记录的计算符号进行计算
# 如果上一个是+，那么就把当前的tmp直接塞进stack
# 如果是-，那么把 -tmp 塞进stack
# 如果是*，那么把 tmp*stack.pop(), 然后结果再放进
# stack里面。
# 如果是/， 那么先看看上一个数字是正还是负数，如果是正数
# 那么直接除，然后把得到的就是一个负数。还是把结果塞进去
# stack
# 最后sum(stack)得出最后结果。