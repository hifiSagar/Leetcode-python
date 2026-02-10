class Solution(object):
    def connect(self, root):
        if not root:
            return None

        leftmost = root

        while leftmost.left:
            head = leftmost
            while head:
                # connect left -> right
                head.left.next = head.right

                # connect right -> next.left
                if head.next:
                    head.right.next = head.next.left

                head = head.next
            leftmost = leftmost.left

        return root
