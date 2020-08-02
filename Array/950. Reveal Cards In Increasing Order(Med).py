#import collections;
#
#deck = [17,13,11,2,3,5,7]
#d = collections.deque()
#for x in sorted(deck)[::-1]:
#    d.rotate()
#    d.appendleft(x)
#print(list(d))
#
#We simulate the reversed process.
#Initial an empty list or deque or queue,
#each time rotate the last element to the first,
#and append a the next biggest number to the left.
