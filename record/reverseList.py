# 翻转一个链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            next_ = cur.next
            cur.next = pre
            pre = cur
            cur = next_
        return pre


def printLink(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    head = ListNode(0)
    cur = head
    for x in range(1, 10):
        node = ListNode(x)
        cur.next = node
        cur = node

    x = Solution().reverseList(head)
    printLink(x)
