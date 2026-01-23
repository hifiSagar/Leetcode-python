from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        leftToRight = True
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if not leftToRight:
                level.reverse()
            
            result.append(level)
            leftToRight = not leftToRight
        
        return result
