'''
61. 旋转链表

给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置
'''
from ds.LinkList import ListNode
def rotateRight(head: ListNode, k: int) -> ListNode:
    if (not head) or (not head.next):
        return head
    pre_p, count_p = head, head
    count = 0
    while count_p:
        pre_p = count_p
        count_p = count_p.next
        count += 1
    pre_p.next = head  # 变环
    k = count - k % count
    count_p = head
    while k:
        pre_p = head
        head = head.next
        k -= 1
    pre_p.next = None
    return head



