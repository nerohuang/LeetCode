class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = [];
        storeCount = 0;
        originLen = len(strs);
        if strs:
            while storeCount != originLen:
                store = [];
                for word in strs:
                    if not store:
                        store.append(word);
                        storeCount += 1;
                    else:
                        if ("".join(sorted(list(word)))) == ("".join(sorted(list(store[0])))):
                            store.append(word);
                            storeCount += 1;
                for word in store:
                    strs.remove(word);
                result.append(store);
                print(store);
            return(result);
        else:
            return('');