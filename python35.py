class Solution:
    def buildTree(self, inorder, postorder):
        idx = {v: i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)

            mid = idx[root_val]
            root.right = helper(mid + 1, r)
            root.left = helper(l, mid - 1)
            return root

        return helper(0, len(inorder) - 1)
