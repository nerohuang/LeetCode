from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        store = defaultdict(list);
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                store[i + j].append(nums[i][j]);
        
        return [v for k in store.keys() for v in reversed(store[k])]

#思路：
#画一个矩阵就知道：
#   0   1   2
#0  1   2   3
#1  4   5   6
#2  7   8   9
#其中1的x + y是0；2， 4 是1+0=1； 3， 5， 7是2+0， 1+1， 0+2=2.。。。
#所以只要把x+y相同的放在一个组里面，然后输出的时候反转就可以了。