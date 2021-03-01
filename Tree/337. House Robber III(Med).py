class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            # return [rob this node, not rob this node]
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            # if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            # else we could choose to either rob its children or not
            not_rob = max(left) + max(right)
            return [rob, not_rob]

        return max(helper(root))



#思路:
#其实也是用DP记录
#抢劫有两种情况:
#1.抢了当前node就不能抢该node的children
#2.不抢当前node就可以抢该node的bhildren
#所以我们就维护一个数[rob，notRob]
#rob的计算方式就是当前node.val加上左右子叶notRob的值
#表明对当前node进行rob，因为对当前node抢劫完，他的子叶
#就不能抢劫了，只能是以notRob的值进行相加。
#notRob的计算方式就是分别找出左右子叶最大的值相加，因为
#当前node不抢劫的话，那么子叶抢不抢都行，找出最大值相加
#就好。