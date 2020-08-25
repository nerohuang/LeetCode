/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    sum = '';
    len1 = num1.length;
    len2 = num2.length;
    carry = 0;
    
    while (len1 > 0 || len2 > 0 || carry == 1){
        num1Digital = +num1.charAt(len1 - 1);
        num2Digital = +num2.charAt(len2 - 1);
        len1--;
        len2--;
        
        curTotal = num1Digital + num2Digital + carry;
        carry = Math.floor(curTotal / 10);
        remainNum = curTotal % 10;
        sum = remainNum + sum;
    }
    
    return sum;
};

/* JS里面charAt如果超过长度的话会返回''，所以可以很好的用于处理，但carry里面保存是1
的时候表示要往前进一位，所以就算长度全部算完了都要确定看看carry里面还有没有1位需要往前 */