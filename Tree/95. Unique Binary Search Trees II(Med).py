class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n)


    def helper(self, start, end):
        if start > end: # edge case, see exposition below
            return [None] 
        
        all_trees = [] # list of all unique BSTs
        for curRootVal in range(start, end+1): # generate all roots using list [start, end]
			# recursively get list of subtrees less than curRoot (a BST must have left subtrees less than the root)
            all_left_subtrees = self.helper(start, curRootVal-1)
			
			# recursively get list of subtrees greater than curRoot (a BST must have right subtrees greater than the root)
            all_right_subtrees = self.helper(curRootVal+1, end) 
			
            for left_subtree in all_left_subtrees:   # get each possible left subtree
                for right_subtree in all_right_subtrees: # get each possible right subtree
                    # create root node with each combination of left and right subtrees
                    curRoot = TreeNode(curRootVal) 
                    curRoot.left = left_subtree
                    curRoot.right = right_subtree
					
					# curRoot is now the root of a BST
                    all_trees.append(curRoot)
		
        return all_trees

#思路：
#根据BST的定律： 左 < 中 < 右
#所以当 i 作为parent的时候， left node的范围就是[1, i - 1] 而right node的范围
#就是[i + 1, n];
#所以我们用递归对所有可能的left node 和 right node进行构造。当递归发现start大于
#end的时候那就说明那个树的构建已经到了尽头，那么就要停止。
#而这里停止为什么是返回[None]而不是一个空是因为返回出来，构建好的左右子树将会参与
#到接下来完整树的构造，而构造完整的树则是以 i 为 root，然后将之前构建好所有符合规则
#的左右子树接在root上面。
#所以如果上面返回空的话，那么那个for就执行不了了。