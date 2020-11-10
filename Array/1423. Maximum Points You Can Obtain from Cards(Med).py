class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        presum = 0;
        postsum = 0;
        
        for i in range(k):
            presum += cardPoints[i];
        
        cursum = presum;
        for i in range(k):
            cursum = cursum - cardPoints[k - 1 - i] + cardPoints[-1 - i];
            presum = max(presum, cursum)
            
        return presum
    
