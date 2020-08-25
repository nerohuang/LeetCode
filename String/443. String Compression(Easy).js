/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    result = [chars[0]];
    count = 1;
    for (let i = 1; i < chars.length; i++){
        if (chars[i - 1] == chars[i]){
            count++;
        }
        else{
            if (count > 1 && count < 10){
                result.push(count.toString(), chars[i]);
            }
            else if(count >= 10){
                result = result.concat(count.toString().split(""), chars[i])
            }
            else{
                result.push(chars[i])
            }
            
            count = 1;
        }
    }
    if (count > 1 && count < 10){
        result.push(count.toString());
    }
    else if(count >= 10){
        result = result.concat(count.toString().split(""))
    }
    for (let i = 0; i < result.length; i++){
        chars[i] = result[i]
    };
    return (result.length);
    
};

/*
var compress = function(chars) {
	
	// var i is reading, var index is writing
    let  i = 0
    let index = 0
    
    while(i < chars.length){
	
        let j = i
        
		// counter for number of same letters
        while(j < chars.length && chars[i] === chars[j]) j++
        
		// write compress letter
        chars[index++] = chars[i]
        
		// write number for compressed letter
        if(j - i > 1){
		
			// if the number is >= 10 the string version will have a length of 2 instead of 1
            let num = (j - i).toString()  
            for(let k = 0; k < num.length; k++){
                chars[index++] = num[k]
            }
        }
		// Even though there are nested while loops the time is N because i is updated to j
        i = j
    }
	
	// Since the "compressing" is done in place index returns the updated version
    return index
};
*/