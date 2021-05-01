def reorganizeString(self, S: str) -> str:
        if not S: return "" 
        # create a counter 
        heap = []
        for key, value in collections.Counter(S).items():
            heapq.heappush(heap,[-value,key])

        res = ""
        pre = heapq.heappop(heap)
        res+= pre[1]

        while heap: 
            curr = heapq.heappop(heap)
            res+=curr[1]

            pre[0]+=1
            if pre[0]<0:
                heapq.heappush(heap,pre)
            pre = curr 

        return "" if len(res)!=len(S) else res

# 思路
# 这道题看看能不能能不能把给出string变成相邻字母不一样的字符串
# 思路没错，就是首先要统计出所有的字符和拥有的个数，然后依次交替
# 把他们从新组成string。
# 至于怎么交替和怎么存储这些数字好，那么最好的是用heap，然后个数
# 要用负数，因为heap的父节点的值只会小于等于所有子节点，所以负数
# 就刚好能反过来了。
# 然后先pop出第一个值pre，也是个数最多的值，然后pop出第二多的cur
# 然后开始交替组成新的string。
# 如果pre的个数还是比零小，意思是还是有多余0的时候，那么把他重新
# push进heap，如果为0那么就不用管，因为他已经没用了。
# 然后把cur当成下一轮的pre，一直到heap没有为止。
# 然后比较新生产的string长度和S的长度
# 如果是一样的那么就返回新产生的string，如果不一样就空
