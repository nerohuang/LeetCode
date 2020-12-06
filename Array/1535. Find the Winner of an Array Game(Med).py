#class Solution:
#    def getWinner(self, arr: List[int], k: int) -> int:
#        count = {};
#        contiune = True;
#        while contiune:
#            if arr[0] == max(arr):
#                return arr[0];
#            if arr[1] == max(arr):
#                return arr[1]
#            if arr[0] > arr[1]:
#                count[arr[0]] = count.get(arr[0], 0) + 1;
#                if count[arr[0]] >= k or count[arr[0]] >= len(arr):
#                    return arr[0];
#                arr = [arr[0]] + arr[2:] + [arr[1]];
#            else:
#                count[arr[1]] = count.get(arr[1], 0) + 1;
#                if count[arr[1]] >= k or count[arr[1]] >= len(arr):
#                    return arr[1];
#                arr = [arr[1]] + arr[2:] + [arr[0]];
#
#=======================以上超时===================

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        count = 0;
        cur = arr[0];
        for i in range(1, len(arr)):
            if cur > arr[i]:
                count += 1;
            else:
                cur = arr[i];
                count = 1;
            if count == k:
                break
        return cur
#思路:
#因为他只要小的就会往最后面塞
#所以其实只要从第一个开始遍历过去就行了
#如果大于下一个就count + 1
#如果小于就取代掉cur，并且count归为1
#因为按照正常顺序这个大于的迟早回到arr[0]
#当count==k的时候就可以可以返回cur
#当循环完之后count没到还是返回cur，因为cur已经是当前arr里面最大的了
#他肯定是唯一可以达成k次的