class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):
            if not node:
                return

            path.append(node.val)

            # Check if it's a leaf and sum matches
            if not node.left and not node.right and remaining == node.val:
                result.append(list(path))  # copy path
            else:
                dfs(node.left, remaining - node.val, path)
                dfs(node.right, remaining - node.val, path)

            path.pop()  # backtrack

        dfs(root, targetSum, [])
        return result
