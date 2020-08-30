/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var reverseStr = function(s, k) {
  currentStore = "";
  storeList = [];
  count = 0;
  i = 0;
  while (i < s.length){
      currentStore = s.substring(i, i + k);
      storeList.push(currentStore.split("").reverse().join(""));
      storeList.push(s.substring(i + k, i + (2 * k)));
      i += 2 * k
  }
  
  return storeList.join("")
};