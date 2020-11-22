class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        begin = [];
        end = [];
        for a, b in paths:
            begin.append(a);
            end.append(b);
        for city in end:
            if city not in begin:
                return city