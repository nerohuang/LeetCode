/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    ans = 0;
    let symbol = new Map();
    symbol.set('I', 1).set('V', 5).set('X', 10).set('L', 50).set('C', 100).set('D', 500).set('M', 1000);
    for (var i = 0; i < s.length; i++){
        if (i <= s.length - 1){
            if (symbol.get(s[i]) < symbol.get(s[i + 1])){
                ans -= symbol.get(s[i]);
            }
            else{
                ans += symbol.get(s[i]);
            }
        }
        else{
            ans += symbol.get(s[i]);
        }
    }
    return ans;
};



/*
var romanToInt = function(s) {
    let data = {
        I:1,
        V:5,
        X:10,
        L:50,
        C:100,
        D:500,
        M:1000
    };
    let sum = 0;
    for(let i=0; i<s.length; i++) {
      let num1 = data[s[i]];
      let num2 = data[s[i+1]]
      if (num2>num1) {
        sum = sum+num2-num1
        i++
      } else {
        sum = sum+num1
      }
    }
   return sum;
    
};
*/