class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        wordFrequency = sorted(word.count(min(word)) for word in words);
        return [len(wordFrequency) - bisect.bisect(wordFrequency, q.count(min(q))) for q in queries];


##bisect用法：
##https://www.cnblogs.com/skydesign/archive/2011/09/02/2163592.html
## 其目的在于查找该数值将会插入的位置并返回，而不会插入