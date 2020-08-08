125. Valid Palindrome/**
* @param {string} s
* @return {boolean}
*/
var isPalindrome = function(s) {
   str = s.replace(/\W/g, "");
   str = str.replace(/_/g, "");
   reversStr = str.split("").reverse().join("");
   
   return str.toLowerCase() == reversStr.toLowerCase();
};

/*练习一下正则表达式。。。。