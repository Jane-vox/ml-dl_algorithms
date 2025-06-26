class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    cur = head
    pre = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

def print_list(head):
    p = head
    while p is not None:
        print(p.val, end=' ')
        p = p.next
    print()

def create_list(ls):
    dummy = ListNode(0)
    curr = dummy
    for val in ls:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    head = create_list([2, 3, 6, 9])

    print_list(head)
    print_list(reverseList(head))

