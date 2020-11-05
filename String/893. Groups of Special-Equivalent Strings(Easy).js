/**
 * @param {string[]} A
 * @return {number}
 */
var numSpecialEquivGroups = function(A) {
    var oddCount = [];
    var evenCount = [];
    const ans = new Set();
    for(let i = 0; i < A.length; i++){
        oddCount = [];
        evenCount = [];
        for(let j = 0; j < A[i].length; j++){
            if (j % 2 == 0){
                oddCount.push(A[i][j]);
            }
            else{
                evenCount.push(A[i][j]);
            }
        }
        oddCount.sort();
        evenCount.sort();
        ans.add(oddCount.join("") + "/" + evenCount.join(""))
        
    }
    
    return ans.size;
};