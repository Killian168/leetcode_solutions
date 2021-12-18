# leetcode submit region begin(Prohibit modification and deletion)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root_node = current_node = ListNode()

        while l1 or l2 or carry:
            l1_val = l2_val = 0

            if l1:
                l1_val = l1.val
                l1 = l1.next

            if l2:
                l2_val = l2.val
                l2 = l2.next

            carry, val = divmod(l1_val + l2_val + carry, 10)
            current_node.next = ListNode(val)
            current_node = current_node.next

        return root_node.next
# leetcode submit region end(Prohibit modification and deletion)
