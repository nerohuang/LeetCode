class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        ans = 0
        for i in range(len(tokens) - 1, -1, -1):
            if tokens[i] in operators:
                stack.append(tokens[i])
            else:
                stack.append(tokens[i])
                while len(stack) >= 3 and stack[-1] not in operators and stack[-2] not in operators:
                    a = int(stack.pop())
                    b = int(stack.pop())
                    operator = stack.pop()
                    if operator == "*":
                        stack.append(a * b)
                    if operator == "+":
                        stack.append(a + b)
                    if operator == "/" and a != 0:
                        stack.append(a / b)
                    if operator == "/" and a == 0:
                        stack.append(0) 
                    if operator == "-":
                        stack.append(a - b)
                            
        return int(stack[0])

# 思路：
# 用栈，比如例子：
# tokens = ["2","1","+","3","*"]
# 计算顺序其实就是 （2 + 1） * 3
# 那么思路就是把这个token反过来遍历，然后
# 跟在运算符后面两个数字便是和运算符相关的两个数字
# 比如[2 1 +]
# 那么就是1 + 2
# 所以当形成这种[num num op]的形式的时候，就可以进行
# 符号运算，然后计算得出的结果要重新push进stack里面
# 作为当前结果运用到以后的计算当中。