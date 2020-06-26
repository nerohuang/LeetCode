class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        count = 1;
        result = []
        for i in range(1, len(S)):
            if S[i] == S[i - 1]:
                count += 1;
                if count >= 3 and i == len(S) - 1:
                    left = i - count + 1;
                    right = i;
                    result.append([left, right]);
            else:
                if count >= 3:
                    left = i - count;
                    right = i - 1;
                    result.append([left, right]);
                count = 1;
        return result

## Solution 1, using a while loop 
#groups = [] 
#count = 1
#size = len(S)
#for i, string in enumerate(S[0:-1]):
#    
#    if S[i] == S[i+1]:
#        count += 1 
#    else:
#        if count >= 3:
#            groups.append([(i-count)+1, i])
#        count = 1 
#if count >= 3: # incase the group is at the end 
#    groups.append([(size -count),size-1])
#
#return groups 