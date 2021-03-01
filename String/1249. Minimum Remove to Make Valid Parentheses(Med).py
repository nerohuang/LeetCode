class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sList = list(s);
        stack = [];
        for i,c in enumerate(sList):
            if c == ')' and stack == []:
                sList[i] = '';
            elif c == '(':
                stack.append((i, c));
            elif c == ')':
                stack.pop();
                
        for i, c in stack:
            sList[i] = '';
            
        return ''.join(sList);

#思路：
#因为要成对，所以会有三种情况:
#1. 碰到 ）， 在他的左边没有（，这样就要去掉
#2. 碰到 （， 那么就把这一个的位置扔进stack
#3. 碰到 ），左边有（，就是stack里面有东西，那么就把最近的一个pop掉

#当遍历完之后，如果stack里面还有，那就是多出来的（
#那就再该位置删掉就可以了。