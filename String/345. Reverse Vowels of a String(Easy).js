/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    vowels = 'aeiouAEIOU'
    char = s.split("")
    i = 0;
    j = s.length;
    while (i < j){
        if (vowels.includes(char[i]) != true && vowels.includes(char[j]) != true){
            i++;
            j--;
        }
        else if (vowels.includes(char[i]) == true && vowels.includes(char[j]) == true){
            char[j] = [char[i], char[i] = char[j]][0];
            i++;
            j--;
        }
        else if (vowels.includes(char[i]) == true && vowels.includes(char[j]) != true){
            j--;
        }
        else if (vowels.includes(char[i]) != true && vowels.includes(char[j]) == true){
            i++;
        }
    }
    return char.join("")
};