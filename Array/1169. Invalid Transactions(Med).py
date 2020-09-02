transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
store = [];
for transcript in transactions:
    name, time, amount, city = transcript.split(",");
    store.append([name, int(time), int(amount), city, transcript]);

ans = set()

for s in store:
    if s[2] > 1000:
        ans.add(s[4]);
        for t in store:
            if s[0] == t[0] and s[3] != t[0] and abs(s[1] - t[1]) <= 60:
                ans.add(t[4])

print(list(ans));

#总体思路就是用冒泡那样直接对比，但是感觉数据大会超时。

#class Transaction(object):
#    def __init__(self, txn):
#        name, time, amount, city = txn.split(',')
#        self.name = name
#        self.time = int(time)
#        self.amount = int(amount)
#        self.city = city
#        
#    def __str__(self):
#        return "{},{},{},{}".format(self.name, self.time, self.amount, self.city)
#    
#class Solution:
#    def invalidTransactions(self, transactions: List[str]) -> List[str]:
#        d = defaultdict(list)
#        ans = set()
#        txns = list(map(Transaction, transactions))
#        for i, t in enumerate(txns):
#            d[t.name].append(i)
#        for name in d:
#            d[name].sort(key=lambda x:txns[x].time)
#        for tid in d.values():    
#            l = r = 0
#            for i, t in enumerate(tid):
#                if txns[t].amount > 1000:
#                    ans.add(t)
#                    continue
#                while l + 1 < len(tid) and txns[tid[l]].time + 60 < txns[t].time:
#                    l += 1
#                while r + 1 < len(tid) and txns[tid[r+1]].time <= txns[t].time + 60:
#                    r += 1
#                for j in range(l, r+1):
#                    if txns[tid[j]].city != txns[t].city:
#                        ans.add(t)
#                        break
#        return [str(transactions[i]) for i in ans]            
            