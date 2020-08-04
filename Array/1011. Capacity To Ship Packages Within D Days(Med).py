def shipWithinDays(self, weights, D):
		low, high = max(weights), sum(weights)
		while low < high:
			# guess the capacity of ship
			mid = (low+high)//2

			cur_cap = 0 # loaded capacity of current ship
			num_ship = 1 # number of ship needed

			#----simulating loading the weight to ship one by one----#
			for w in weights:
				cur_cap += w
				if cur_cap > mid: # current ship meets its capacity
					cur_cap = w
					num_ship += 1
			#---------------simulation ends--------------------------#

			# we need too many ships, so we need to increase capacity to reduce num of ships needed
			if num_ship > D:
				low = mid+1
			# we are able to ship with good num of ships, but we still need to find the optimal max capacity
			else:
				high = mid

		return low


1.这里， 每天最少的运力应该至少是货物的最大重量， 否则这个最重的货物就无法运输了
2.最大的运力就是所有货物的重量和， 相当于一天之内全部运完了
3.那么，我们确定了这个解的上限和下限， 那么，可以用二分搜索来查找符合要求的最佳解
4.给定一个运力， 我们需要计算需要多少天可以把货物运输完。 按顺序计算目前的重量， 如果超时了就重新开始一天就好
5.对于任何一个运力，知道需要多少天以后，我们需要修改上限和下限， 这里需要仔细一点，
– 如果middays < D, 那就不符合要求，运力太少了，运力一定是需要增加， 那么一定是low=mid+1
– 如果middays == D, 那有可能当前的运力是答案， 因为可能运力减少1以后就不符合要求了， 所以这里设置high=mid
– 如果middays > D, 同样，这时候也应该设置high=mid, 因为运力减少1以后也有可能不符合要求