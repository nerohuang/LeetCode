class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if not votes: return
        # Create a dict storing the letter as key and cnt the ranks for each.
        ranks = collections.defaultdict(lambda: [0]*len(votes[0]))
        # Run through all of the votes, use - cnt for our sort.
        for i in votes:
            for idx, l in enumerate(i):
                ranks[l][idx] -= 1
        # Sort by - cnt and key.
        srt = dict(sorted(ranks.items(), key=lambda x: (x[1], x[0])))
        # Join all of the sorted keys and we're done.
        return ''.join(srt.keys())

#思路：
#他妈原理python的sort这么牛逼能sort多维数组并且能根据每一位来sort！
#所以他妈就记录每一个队他在第几位得票然后sort就行了!
#大概就这样了[[0, 0, 1, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 0, 0]]
#然后就是sorted和lambda的用法了！