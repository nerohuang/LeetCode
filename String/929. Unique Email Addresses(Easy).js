/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    const ans = new Set();
    for (let i = 0; i < emails.length; i++){
        domainLoc = emails[i].indexOf("@");
        domain = emails[i].substring(domainLoc);
        name = emails[i].substring(0, domainLoc)
        nameStore = name.split("");
        reName = [];
        for (let i = 0; i < nameStore.length; i++){
            if (nameStore[i] == "+"){
                break;
            }
            if (nameStore[i] != "."){
                reName.push(nameStore[i]);
            }
        }
        
        ans.add(reName.join("") + domain);
    }
    
    return ans.size;
};

/*
var numUniqueEmails = function(emails) {
    const set = new Set();
    
    for(var email of emails){
        let arr= email.split("@");
        arr[0] = (arr[0].split("+"))[0];
        arr[0] = arr[0].replace(/\./g, "");
        set.add(arr.join("@")); 
    }
    return set.size;
    
};
*/