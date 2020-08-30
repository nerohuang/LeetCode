/**
 * @param {string} A
 * @param {string} B
 * @return {number}
 */
var repeatedStringMatch = function(A, B) {
    if (A.includes(B)){
        return 1
    }
    time = Math.floor(B.length / A.length);
    A = A.repeat(time)
    console.log(time)
    console.log(A)
    if (A.includes(B)){
        return time
    }
    else{
        A += A;
        if (A.includes(B)){
            return time + 1
        }
    }
    
    return -1
};