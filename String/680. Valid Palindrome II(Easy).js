/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function(s) {
    if (s == s.split("").reverse().join("")){
        return true
    }
    for (let i = 0; i < s.length; i++){
        if (s[i] != s[s.length -1 - i]){
            return (palindrome(s, i) || palindrome(s, s.length -1 -i));
        }
    }
    
    function palindrome(s, i){
        store = s.substring(0, i) + s.substring(i + 1);
        return (store == store.split("").reverse().join(""));
    }
};

/*
思路：求删除一个是不是回文，那么就寻找到哪一位和他对应的位字母不一样，删除掉之后倒转的对比，
如果相同就是，不相同就不是



var validPalindrome = function(str, deleteCharMax = 1) {
    
    let i = 0;
    let j = str.length - 1;
    
    while(i < j) {
        
        if(str[i] === str[j]) {
            
            i++;
            j--;
            continue;
        }
        
        if(deleteCharMax === 0) {
            return false;
        }
        
        return validPalindrome(str.slice(i, j), 0) || validPalindrome(str.slice(i+1, j+1), 0);
    }
    
    return true;
};


*/