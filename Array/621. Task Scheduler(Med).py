import collections;

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = list(collections.Counter(tasks).values())
        max_count = max(tasks_count)
        max_count_tasks = tasks_count.count(max_count)
        return max(len(tasks), (max_count-1)*(n+1)+max_count_tasks)


#Let's say the most frequent tasks occur M times, and there are Mct of them.
#
#When N > Mct, let's make our scheduling constraint strictly stronger by choosing 
#N = Mct. So from now on, let's suppose Mct <= N, and the most frequent tasks are 
#denoted #A, #B, #C, ... #K.
#
#Then we could schedule say, ABC...K__..._ABC...K__..._ABC...K__....., 
#where A...K occurs Mct times, _ denotes idle time, and there is N space between A's. 
#This partial schedule would have length L = (M-1) * (N+1) + Mct. Clearly, we need at 
#least L intervals of time in our schedule to fit our given tasks. Let's show this is 
#enough.

#from heapq import heappush, heappop
#from collections import Counter
#class Solution:
#    def leastInterval(self, tasks, n):
#        """
#        :type tasks: List[str]
#        :type n: int
#        :rtype: int
#        """
#        curr_time, h = 0, []
#        for k,v in Counter(tasks).items():
#            heappush(h, (-1*v, k))
#        while h:
#            i, temp = 0, []
#            while i <= n:
#                curr_time += 1
#                if h:
#                    x,y = heappop(h)
#                    if x != -1:
#                        temp.append((x+1,y))
#                if not h and not temp:
#                    break
#                else:
#                    i += 1
#            for item in temp:
#                heappush(h, item)
#        return curr_time
#
#This is an extremely tricky problem.
#The main idea is to schedule the most frequent tasks as frequently as possible. 
#Begin with scheduling the most frequent task. Then cool-off for n, and in that 
#cool-off period schedule tasks in order of frequency, or if no tasks are available, 
#then be idle.
#Exampe: Say we have the following tasks: [A,A,A,B,C,D,E] with n =2
#Now if we schedule using the idea of scheduling all unique tasks once and then 
#calculating if a cool-off is required or not, then we have: A,B,C,D,E,A,idle,dile,
#A i.e. 2 idle slots.
#But if we schedule using most frequent first, then we have:
#2.1: A,idle,idle,A,idle,idle,A
#2.2: A,B,C,A,D,E,A i.e. no idle slots. This is the general intuition of this problem.
#3.The idea in two can be implemented using a heap and temp list. This is illustrated 
#in the code below.
#4.Time complexity is O(N * n) where N is the number of tasks and n is the cool-off 
#period.
#5.Space complexity is O(1) - will not be more than O(26).