class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        frequency = {};
        for i in range(k):
            frequency[i] = frequency.get(i, 0);
        for num in arr:
            frequency[(num % k)] = frequency.get((num % k), 0) + 1;
        ans = True;
        for freq in frequency:
            if freq == 0 and frequency[freq] != 0:
                ans = True if frequency[freq] % 2 == 0 else False;
            elif freq != 0 and frequency[freq] != frequency[k - freq]:
                ans = False;
                break;
        return ans

#思路:
#数学题，我脑抽了
#因为加起来是k的倍数，所以这一对的数除以K的余数相加肯定等于k
#那么就现在建立一个k长度的数组frequency记录所有可能的余数
#出现的次数
#然后如果 freq[i] == freq[k - i]那么表示拥有这两个余数
#结果的数是相等的，那么那么都可以组成一组得到是k的倍数。
#如果不一样，那么表明有多的无法组成，那么就错了。
#注意余数为0的，余数为0表示本来就是k的倍数，那么只能和
#其他余数为0的相加，所以如果freq[0]大于0而且不是偶数
#（不能组队）的话，那么就错了。