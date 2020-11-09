/**
 * @param {string[]} logs
 * @return {string[]}
 */
var reorderLogFiles = function (logs) {
    let letters = [];
    let digits = [];
    for (let i = 0; i < logs.length; i++) {
        const current = logs[i].split(' ');
        if (isNaN(parseInt(current[current.length - 1]))) letters.push(logs[i]);
        else digits.push(logs[i]);
    }
    return (
        letters.sort((a, b) => {
            if (a.substring(a.indexOf(' ')) < b.substring(b.indexOf(' '))) return -1;
            else if (a.substring(a.indexOf(' ')) > b.substring(b.indexOf(' '))) return 1;
            else {
                if (a < b) return -1;
                else if (a > b) return 1;
            };
        }).concat(digits)
    )
};