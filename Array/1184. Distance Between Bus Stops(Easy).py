class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start;
        sumClock = sum(distance[start:destination]);
        sumTotal = sum(distance);
        sumCounterClock = sumTotal - sumClock;
        return sumClock if sumCounterClock > sumClock else sumCounterClock;

##class Solution:
##    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
##        lower = min(start, destination)
##        upper = max(start, destination)
##        s_1 = sum(distance[lower:upper])
##        return min(
##            s_1, 
##            sum(distance) -s_1
##        )