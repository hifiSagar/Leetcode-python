class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            # Path including both sides
            self.max_sum = max(self.max_sum, left + right + node.val)
            
            # Return one side only
            return node.val + max(left, right)
        
        dfs(root)
        return self.max_sum