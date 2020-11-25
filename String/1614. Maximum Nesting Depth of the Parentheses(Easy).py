class Solution:
def maxDepth(self, s: str) -> int:
    stack = []
    depth = 0
    
    for char in s:
	    # Add to stack is you see open bracket
        if char == "(":
            stack.append("(")
		
		# Pop from stack if you see closing bracket and last element on the stack is "("
        if char == ")" and stack[-1] == "(":
            
			# Increment the depth if len(stack) > depth
			if len(stack) > depth:
                depth = len(stack)
            
			# Perform stack pop
			stack.pop()
    
	# Return depth
    return depth