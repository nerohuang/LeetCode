/**
 * @param {string} name
 * @param {string} typed
 * @return {boolean}
 */
var isLongPressedName = function(name, typed) {
    typedCount = [];
    nameCount = [];
    count = 1;
    for (let i = 1; i <= name.length; i++){
        if (name[i - 1] == name[i]){
            count ++;
        }else{
            nameCount.push([name[i - 1], count]);
            count = 1;
        }
    }
    
    count = 1;
    for (let i = 1; i <= typed.length; i++){
        if (typed[i - 1] == typed[i]){
            count ++;
        }else{
            typedCount.push([typed[i - 1], count]);
            count = 1;
        }
    }
    
    if (typedCount.length != nameCount.length){
        return false
    }
    else{
        for (let i = 0; i < nameCount.length; i++){
            if (typedCount[i][0] != nameCount[i][0] || typedCount[i][1] < nameCount[i][1]){
                return false
            }
        }
    }
    
    return true
};