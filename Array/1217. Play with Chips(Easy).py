class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        count = [0, 0];
        for chip in chips:
            count[chip % 2] += 1;
        return min(count);

#Since no cost to move even steps, all elements at even/odd indices can move to index 0/1 respectively without cost;
#Compare the count of elements at index 0 with that at 1, each of them need cost 1 to move to index 1/0 respectively; return the lesser.

##class Solution:
##    def minCostToMoveChips(self, chips: List[int]) -> int:
##        ans=float('inf')
##        oddCount=0
##        evenCount=0
##        for i in range(len(chips)):
##            if chips[i]%2==0:
##                evenCount+=1
##            else:
##                oddCount+=1
##        return min(evenCount,oddCount)