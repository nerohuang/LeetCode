/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
    codeStore = [];
    for (let i = 0; i < words.length; i++){
        decode = "";
        word = words[i];
        for (let j = 0; j < word.length; j++){
            decode += code[(word[j].charCodeAt() - 97)];
        }
        if (codeStore.includes(decode) != true){
            codeStore.push(decode)
        }
    }
    
    return codeStore.length;
};