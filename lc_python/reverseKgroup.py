'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from ds.LinkList import ListNode
def reverseKGroup(self, head, k: int) ->ListNode :
    if not head:
        return []
    if k == 1:
        return head
    p, head.next = head.next, None
    tail, count = head, k - 1
    while count:
        tmp, p = p, p.next
        tmp.next = head
        head = tmp
        count -= 1
    while p:
        # 检查剩余的够k 否 ？
        cp = p
        for i in range(k):
            if cp is None:
                tail.next = p
                return head
            cp = cp.next
        h_t = tail
        tail = p
        for i in range(k):
            if p is None:
                return head
            tmp, p = p, p.next
            tmp.next = h_t.next
            h_t.next = tmp
    return head

def reverseKGroup(self, head, k: int) ->ListNode :
    def reverse(head):
        if (not head) or (not head.next):
            return head, head
        cur, head.next = head.next, None
        tail = head
        while cur:
            tmp = cur
            cur = cur.next
            tmp.next = head
            head = tmp
        return head, tail
    ##########
    if k == 1 or (not head) or (not head.next):
        return head
    rhead = ListNode()
    tail = rhead
    pre, countp = None, head
    while countp:
        cur = countp
        for i in range(k):
            if countp is None:  # 数不够k个
                tail.next = cur
                return rhead.next
            pre = countp
            countp = countp.next
        pre.next = None
        tail.next, tail = reverse(cur)
    return rhead.next