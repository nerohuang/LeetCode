maxChoosableInteger = 3;
desiredTotal = 5

def dfs_rec_memo(total, num_used):
    
    if( tuple(num_used) in cache ):
        return cache[ tuple(num_used) ]
    
    for num in range(1, maxChoosableInteger + 1):
        # 如果遍历到的数字没有选过
        if( not num_used[num] ) :
            # 如果当前数字加上当前总和大于target
            if(total + num >= desiredTotal ):
                #记录下当前的选择，然后返回True（胜利）
                cache[ tuple(num_used) ] = True
                return True
            
            #如果没有，记录下当前数字变为已经选过
            num_used[num] = True
            # 如果下一个人返回false，我们才能继续选择
            if ( not dfs_rec_memo( total + num, num_used ) ):
                # make sure to back track, here also before returning
                # 我们把现在选择的数字从新变为False来用于下次遍历
                num_used[num] = False   
                # 但是同时也要记录这次因为接下来的所有可能性都已经寻找过了
                # 并且得到的结果是赢了
                cache[ tuple(num_used) ] = True
                return True
            # backtrack

            
            num_used[num] = False
    
    # 如果遍历完都还是屁都没赢，当前可能性记录下来并且为false
    cache[ tuple(num_used) ] = False
    return False

#if(1+maxChoosableInteger)*maxChoosableInteger//2 < desiredTotal:
#    return False

cache = {}
num_used = [False] * (maxChoosableInteger + 1)
ans =  dfs_rec_memo(0, num_used)
print(ans)
# DFS
# 并不能算是一道dp题目
# 题目是player 1和player 2互相选数字然后不重复，看看谁能最先到达目标数字
# 那么取胜方式是：你选的数字能大于目标数字，然后确保对方选的不能获胜
# 那么就用DFS看看所有有可能的选择肢最后能不能赢就行了。
# 因为假设两个玩家都是走最优解，所以其实就是看所选的数字总和有没有超过目标
# 然后同时建立一个set来记录曾经博弈过的可能性来减少时间。