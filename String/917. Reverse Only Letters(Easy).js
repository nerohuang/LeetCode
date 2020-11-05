/**
 * @param {string} S
 * @return {string}
 */
var reverseOnlyLetters = function(s) {
    char = [];
    pun = [];
    punLoc = [];
    for (let i = 0; i < s.length; i++){
        if ((s.charCodeAt(i) >= 65 && s.charCodeAt(i) <=90) || (s.charCodeAt(i) >= 97 && s.charCodeAt(i) <= 122)){
            char.push(s[i]);
        }
        else{
            pun.push(s[i]);
            punLoc.push(i);
        }
    }
    ans = char.reverse().join("");
    for (let i = 0; i < punLoc.length; i++){
        ans = ans.substring(0, punLoc[i]) + pun[i] + ans.substring(punLoc[i]);
    }
    return ans;
};