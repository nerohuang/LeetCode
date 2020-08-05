/** 
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    read = '1';
    for (let i = 1; i < n; i++){
        readSplit = read.split("");
        read = ''
        count = 1;
        for (let j = 0; j < readSplit.length; j++){
            if (readSplit[j] !== readSplit[j + 1]){
                read += count + readSplit[j];
                count = 1;
            }
            else{
                count++;
            }
        }
    }
    return read;
}