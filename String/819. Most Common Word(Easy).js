/**
 * @param {string} paragraph
 * @param {string[]} banned
 * @return {string}
 */
var mostCommonWord = function(paragraph, banned) {
    paragraph = paragraph.replace(/\W+/gi,' ');
        
    words = paragraph.split(" ");
    
    const wordCount = {};
    
    for(let word of words){
        word = word.toLowerCase();
        if (!banned.includes(word)){
            if (!wordCount[word]){
                wordCount[word] = 0;
            }
            wordCount[word]++;
        }
    }
    
    maxCount = 0;
    ans = '';
    for (let word of Object.keys(wordCount)){
        word = word.toLowerCase();
        if (wordCount[word] > maxCount){
            ans = word;
            maxCount = wordCount[word] ;
        };
    };
    
    return ans;
};