/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    uCount = 0;
    dCount = 0;
    lCount = 0;
    rCount = 0;
    for (let i = 0; i < moves.length; i++){
        if (moves[i] == "U"){
            uCount += 1;
        }
        if (moves[i] == "D"){
            dCount += 1;
        }
        if (moves[i] == "L"){
            lCount += 1;
        }
        if (moves[i] == "R"){
            rCount += 1;
        }
        
    }
    if (uCount == dCount && lCount == rCount){
        return true
    }
    
    return false
};