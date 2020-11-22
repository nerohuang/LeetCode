class Solution:
    def isPathCrossing(self, path: str) -> bool:
        point = [[0, 0]];
        x = 0;
        y = 0;
        for step in path:
            if step == "N":
                x += 1;
            if step == "S":
                x -= 1;
            if step == "E":
                y += 1;
            if step == "W":
                y -= 1;
            if [x, y] in point:
                return True;
            point.append([x, y])