/**
 * @param {string} s
 * @return {number}
 */
var countSegments = function(s) {
    str = s.split(" ");
    count = 0;
    for (let charter of str){
        if (charter != " " && charter != ""){
            count++;
        }
    }
    return count;
};