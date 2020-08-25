/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    if (word == word.toUpperCase() || word == word.toLowerCase()){
        return true
    }
    if (word[0] == word[0].toUpperCase()){
        if (word.substring(1) == word.substring(1).toLowerCase()){
            return true;
        }
    }
    return false
};