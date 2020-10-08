/**
 * @param {number} N
 * @return {number}
 */
var rotatedDigits = function(N) {
    var numRotate = {
        "1":"1",
        "2":"5",
        "5":"2",
        "6":"9",
        "8":"8",
        "9":"6",
        "0":"0"
    };
    ans = 0;
    for (let i = 1; i <= N; i++){
        strNum = i.toString();
        newStr = "";
        for (let j = 0; j < strNum.length; j++){
            if (numRotate.hasOwnProperty(strNum[j])){
                newStr += numRotate[strNum[j]];
            }
            else{
                break;
            }
        };
        if (strNum.length == newStr.length && strNum != newStr){
            ans += 1;
        }
    };
    
    return ans;
};