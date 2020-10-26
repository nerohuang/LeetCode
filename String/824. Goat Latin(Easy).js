/**
 * @param {string} S
 * @return {string}
 */
var toGoatLatin = function(S) {
    store = S.split(" ");
    ans = [];
    
    for (let i = 0; i < store.length; i++){
        aCount = "";
        for (let j = 0; j < i + 1; j++){
            aCount += "a";
        }
        if ("aeiou".includes(store[i][0].toLowerCase())){
            ans.push(store[i] + "ma" + aCount);
        }
        
        else{
            word = store[i].substring(1) + store[i][0] + "ma" + aCount;
            ans.push(word);
        }
    }
    
    return ans.join(" ");
};