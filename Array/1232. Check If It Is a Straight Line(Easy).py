class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (coordinates[0][0] == coordinates[1][0]):
            k = None;
        else:
            k = (coordinates[0][1] - coordinates[1][1])/(coordinates[0][0] - coordinates[1][0]);
        for i in range(1, len(coordinates) - 1):
            if coordinates[i][0] != coordinates[i + 1][0]:
                if k != (coordinates[i][1] - coordinates[i + 1][1])/(coordinates[i][0] - coordinates[i + 1][0]):
                    return False;
            else:
                if k != None:
                    return False;
        return True;


##class Solution:
##    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
##        if len(coordinates) == 2 :
##            return True
##        if (coordinates[1][0] - coordinates[0][0]) == 0:
##            for i in range(2,len(coordinates)):
##                if coordinates[i][0] != coordinates[0][0]:
##                    return False
##        else:
##            k = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
##            b = coordinates[0][1] - (coordinates[0][0] * k) 
##            for i in range(2,len(coordinates)):
##                if (coordinates[i][0] * k + b) != coordinates[i][1]:
##                    return False
##            return True