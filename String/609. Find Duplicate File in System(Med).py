class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = defaultdict(set);
        for path in paths:
            files = path.split(" ");
            for i in range(1, len(files)):
                content = '';
                loc = 0;
                for j in range(len(files[i]) - 1, -1, -1):
                    if files[i][j] == '(':
                        loc = j;
                        break;
                    content += files[i][j];
                store[content].add(files[0]+"/"+files[i][:j]);
        ans = [];
        for key in store.keys():
            if len(store[key]) >= 2:
                ans.append(list(store[key]));
        return ans

#憨逼问题。。。