# 合并两条链表

import random

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge(one, two):
    head = point = ListNode(-1)
    while one and two:
        if one.val < two.val:
            point.next = one
            one = one.next
            point = point.next
        else:
            point.next = two
            two = two.next
            point = point.next

    if one:
        point.next = one
    else:
        point.next = two
    return head.next

def printList(head):
    while head:
        print(head.val, end = " ")
        head = head.next
    
    print("")

if __name__ == "__main__":
    one = pOne = ListNode(-1)
    two = pTwo = ListNode(-1)

    node = ListNode(35)
    pOne.next = node

    printList(one.next)
    print("-------------one-------------")

    for _ in range(2):
        node = ListNode(random.randint(0, 1000))
        pTwo.next = node
        pTwo = pTwo.next

    printList(two.next)
    print("-------------two-------------")

    theHead = merge(one.next, two.next)

    printList(theHead)
    