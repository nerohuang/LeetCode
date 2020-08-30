/**
 * @param {string} s
 * @return {boolean}
 */
var checkRecord = function(s) {
    aCount = 0;
    lCount = 0;
    for (let i = 0; i < s.length; i++){
        if (s[i] != 'L'){
            lCount = 0;
        }
        if (s[i] == 'A'){
            aCount += 1;
            if (aCount > 1){
                return false;
            }
        }
        if (s[i] == 'L'){
            lCount += 1;
            if (lCount > 2){
                return false;
            }
        }
    }
    
    return true;
};