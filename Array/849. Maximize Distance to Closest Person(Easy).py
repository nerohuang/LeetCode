class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxDistance = 0;
        for i in range(len(seats)):
            if seats[i] == 0:
                if i > 0:
                    if 1 in seats[i:]:
                        if (seats[i - 1] == 1):
                            distance = seats[i:].index(1);
                            if distance == 2:
                                maxDistance = max(maxDistance, 1);
                            elif (distance%2 == 0):
                                maxDistance = max(maxDistance, (distance//2));
                            else:
                                maxDistance = max(maxDistance, (distance//2) + 1);
                    else:
                        if (seats[i - 1] == 1):
                            maxDistance = max(maxDistance, len(seats) - i);
                else:
                    maxDistance = max(maxDistance, seats[i:].index(1) - i);
        return maxDistance;


##class Solution:
##    def maxDistToClosest(self, seats: List[int]) -> int:
##        maxdis = 0
##        count = 0
##        dis = []
##        
##        if seats.count(1)==1:
##            return max(abs(0-seats.index(1)),abs(seats.index(1)-len(seats)+1))
##        else:
##            for each in seats:
##                if each == 0:
##                    count+=1
##                else:
##                    break
##            dis.append(count)
##            count = 0
##            for each in seats[::-1]:
##                if each == 0:
##                    count+=1
##                else:
##                    break
##            dis.append(count)
##            for i in range(len(seats)):
##                if seats[i]==0:
##                    count+=1
##                else:
##                    dis.append((count+1)//2)
##                    count = 0
##            return max(dis)       