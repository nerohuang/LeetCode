class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0;

#class Solution:
#    def divisorGame(self, N: int) -> bool:
#        dict_bool = {} # This our memoization table
#        
#        def ways(num, player):
#            if num == 1 and player=='B': # No move left for Bob
#                return True
#            if num == 1 and player=='A':  # No move left for Alice
#                return False
#            
#            if num in dict_bool: # Check whether num is already in dict_bool
#                return
#            
#			# Flipping players each turn 'A' - Alice, 'B' - Bob
#            if player == 'A':
#                player = 'B'
#            else:
#                player = 'A'
#                
#            # Get divisors
#            to_check = []
#            for i in range(1, (num//2)+1):
#                if num % i == 0:
#                    to_check.append(num-i)
#            
#            for check in to_check: # Start branching off for each divisor
#                dict_bool[num] = ways(check, player)
#				# ^---- Memoize the reults there
#				
#        ways(N, 'A')
#        return any(dict_bool.values())

#思路：
#有两种做法:
#一种是数学题，只要是偶数先走的必赢，只要是奇数先走的必输
#因为偶数开头的话最后都能弄成N = 2然后A开始走的情况，反之
#亦然。
#第二种就是DP，用递归寻找全部步数的可能性。
#如果全部都可能那么才能赢。