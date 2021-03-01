class Solution:
    def simplifyPath(self, path: str) -> str:
        store = ["/"];
        cur = "";
        for i in range(len(path)):
            if path[i] == "/":
                if cur:
                    if cur == "/..":
                        if len(store) != 1:
                            store.pop();
                    elif cur != "/" and cur != "/.":
                        store.append(cur);
                    cur = "";
                cur += path[i];
            else:
                cur += path[i];
        
        if cur:
            if cur == "/..":
                if len(store) != 1:
                    store.pop();
            elif cur != "/" and cur != "/.":
                store.append(cur);
            cur = "";
        if len(store) > 1:
            del store[0];
                
        return "".join(store);

#Split,split,split!!!!!!!!!
#class Solution:
#    def simplifyPath(self, path: str) -> str:
#        result = []
#        
#        for folder in path.split('/'):
#            if folder == '..':
#                if result:
#                    result.pop()
#            elif folder and folder is not '.':
#                result.append(folder)
#        
#        return f'/{"/".join(result)}'