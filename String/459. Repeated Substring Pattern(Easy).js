/**
 * @param {string} s
 * @return {boolean}
 */
var repeatedSubstringPattern = function(s) {
    
    reLoc = 0;
    if (s.length < 2){
        return false
    };
    
    half = Math.floor(s.length/2);
    
    for (i = half; i >= 1; i--){
        captrue = s.substring(0, i);
        res = s.split(captrue).join("");
        if (res.length == 0){
            return true;
        }
    }
    
    return false;
    
    
    /*
    reLoc = s.indexOf(s[0], 1);
    captrue = s.substring(0, reLoc)
    res = s.split(captrue).join("")
    if (res.length == 0){
        return true
    }
    else{
        return false
    }
    */
};



/*
var repeatedSubstringPattern = function(s) {
    return (s+s).substring(1, 2 * s.length - 1).indexOf(s) >= 0;
};
*/