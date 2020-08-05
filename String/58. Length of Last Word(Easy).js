/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    return s.trim().split(" ").pop().length;
};

/*
trim : 
Remove whitespace from both sides of a string:
*/