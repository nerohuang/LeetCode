/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    for (let i = 0; i < s.length; i++){
        if (s[i] == '(' || s[i] == '[' || s[i] == '{'){
            stack.push(s[i]);
        }
        else{
            curBrackets = stack.pop();
            if (s[i] == ')' && curBrackets != '('){
                return false;
            }
            else if (s[i] == ']' && curBrackets != '['){
                return false;
            }
            else if (s[i] == '}' && curBrackets != '{'){
                return false;
            }
        }
    }
    if (stack.length == 0){
        return true;
    }
    else{
        return false;
    }
};

/*
思路：
把每一个左括号放进一个栈，然后遇到任意一个右括号的时候弹出第一个查看是不是对称。
*/

/*
var isValid = function(s) {
    if(!s || s.length === 0) return true;
    let stack = [ ];
    let map = { '}': '{', ')': '(',']': '[' }
    
    for(let i = 0; i < s.length; i++){
        if("{([".includes(s[i])) stack.push(s[i])
        
        else{
            if(stack.top() === map[s[i]]) stack.pop()
            else return false
        }
    }
    
    return stack.length === 0
};
*/